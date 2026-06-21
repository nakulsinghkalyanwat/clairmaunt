const { createClient } = require('@supabase/supabase-js');
const validator = require('validator');
const xss = require('xss');

// Fallback configuration if env variables are not present
const DEFAULT_SUPABASE_URL = 'https://tgjemawospfmczctkrpp.supabase.co';
const DEFAULT_SUPABASE_ANON_KEY = 'sb_publishable_Zw2QZQyGUVLHqJ8yFZZrtw_B1Editz9';

module.exports = async (req, res) => {
  // 1. Method check: POST only
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const {
      name,
      company,
      email,
      phone,
      city,
      state,
      industry,
      service_type,
      bottle_size,
      design_req,
      qr_req,
      delivery_date,
      delivery_loc,
      campaign_obj,
      ad_event,
      audience,
      quantity,
      frequency,
      source,
      details
    } = req.body || {};

    // 2. Retrieve client IP address
    const ip = req.headers['x-real-ip'] || req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1';

    // 3. Initialize Supabase Client
    const supabaseUrl = process.env.SUPABASE_URL || DEFAULT_SUPABASE_URL;
    // Prefer service role key, but fallback to anon key for easy local testing
    const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || DEFAULT_SUPABASE_ANON_KEY;
    const supabase = createClient(supabaseUrl, supabaseKey);

    // 4. Rate Limiting check: Max 5 submissions per IP within 15 minutes
    let hasIpColumn = true;
    const fifteenMinutesAgo = new Date(Date.now() - 15 * 60 * 1000).toISOString();

    const { count, error: countError } = await supabase
      .from('quotes')
      .select('*', { count: 'exact', head: true })
      .eq('ip_address', ip)
      .gt('created_at', fifteenMinutesAgo);

    if (countError) {
      console.warn('Supabase rate limit query returned error (graceful degradation activated):', JSON.stringify(countError));
      hasIpColumn = false;
    }

    if (hasIpColumn && count !== null && count >= 5) {
      return res.status(429).json({ error: 'Too many requests. You can submit up to 5 quotes every 15 minutes. Please try again later.' });
    }

    // 5. Bot Protection: Cloudflare Turnstile token validation disabled


    // 6. Validation & Length Constraints
    // Required fields check
    if (!name || validator.isEmpty(name.trim())) return res.status(400).json({ error: 'Full Name is required.' });
    if (!company || validator.isEmpty(company.trim())) return res.status(400).json({ error: 'Company / Organization is required.' });
    if (!email || validator.isEmpty(email.trim())) return res.status(400).json({ error: 'Email Address is required.' });
    if (!phone || validator.isEmpty(phone.trim())) return res.status(400).json({ error: 'Phone Number is required.' });
    if (!city || validator.isEmpty(city.trim())) return res.status(400).json({ error: 'City is required.' });
    if (!state || validator.isEmpty(state.trim())) return res.status(400).json({ error: 'State is required.' });
    if (!industry || validator.isEmpty(industry.trim())) return res.status(400).json({ error: 'Industry is required.' });
    if (!service_type || validator.isEmpty(service_type.trim())) return res.status(400).json({ error: 'Service selection is required.' });
    if (!quantity || validator.isEmpty(quantity.trim())) return res.status(400).json({ error: 'Quantity is required.' });
    if (!frequency || validator.isEmpty(frequency.trim())) return res.status(400).json({ error: 'Expected requirement frequency is required.' });

    // Validate email format
    if (!validator.isEmail(email)) {
      return res.status(400).json({ error: 'Please enter a valid email address.' });
    }

    // Validate phone number format (Allow standard international/Indian phone formats, min 7, max 20 chars)
    const phoneRegex = /^\+?[0-9\s\-+\(\)]{7,20}$/;
    if (!phoneRegex.test(phone.trim())) {
      return res.status(400).json({ error: 'Please enter a valid phone number.' });
    }

    // Check string length limits to prevent payload flooding / database overflow
    if (name.length > 100) return res.status(400).json({ error: 'Full Name must be under 100 characters.' });
    if (company.length > 100) return res.status(400).json({ error: 'Company / Organization must be under 100 characters.' });
    if (email.length > 100) return res.status(400).json({ error: 'Email must be under 100 characters.' });
    if (phone.length > 20) return res.status(400).json({ error: 'Phone Number must be under 20 characters.' });
    if (city.length > 100) return res.status(400).json({ error: 'City must be under 100 characters.' });
    if (state.length > 100) return res.status(400).json({ error: 'State must be under 100 characters.' });
    if (industry.length > 50) return res.status(400).json({ error: 'Industry value is invalid.' });
    if (service_type.length > 50) return res.status(400).json({ error: 'Service selection value is invalid.' });
    
    if (bottle_size && bottle_size.length > 50) return res.status(400).json({ error: 'Bottle size value is invalid.' });
    if (design_req && design_req.length > 50) return res.status(400).json({ error: 'Design requirement value is invalid.' });
    if (qr_req && qr_req.length > 50) return res.status(400).json({ error: 'QR requirement value is invalid.' });
    
    if (delivery_date) {
      if (delivery_date.length > 20) return res.status(400).json({ error: 'Delivery date is invalid.' });
      // Validate delivery_date format as YYYY-MM-DD
      const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
      if (!dateRegex.test(delivery_date)) {
        return res.status(400).json({ error: 'Delivery date format must be YYYY-MM-DD.' });
      }
    }

    if (delivery_loc && delivery_loc.length > 200) return res.status(400).json({ error: 'Delivery address must be under 200 characters.' });
    if (campaign_obj && campaign_obj.length > 50) return res.status(400).json({ error: 'Campaign objective value is invalid.' });
    if (ad_event && ad_event.length > 50) return res.status(400).json({ error: 'Preferred event value is invalid.' });
    if (audience && audience.length > 500) return res.status(400).json({ error: 'Target audience must be under 500 characters.' });
    if (quantity.length > 50) return res.status(400).json({ error: 'Quantity value is invalid.' });
    if (frequency.length > 50) return res.status(400).json({ error: 'Frequency value is invalid.' });
    if (source && source.length > 50) return res.status(400).json({ error: 'Source selection is invalid.' });
    if (details && details.length > 1000) return res.status(400).json({ error: 'Additional notes must be under 1000 characters.' });

    // Validate enum choices to prevent tampered requests
    const validIndustries = ['Hotel', 'Resort', 'Restaurant', 'Cafe', 'Wedding Planner', 'Event Organizer', 'Corporate', 'Sports Organization', 'Educational Institution', 'Real Estate', 'Healthcare', 'Other'];
    if (!validIndustries.includes(industry)) return res.status(400).json({ error: 'Invalid Industry selected.' });

    const validServices = ['Customized Water Bottles', 'Advertise On Bottles', 'Both Services'];
    if (!validServices.includes(service_type)) return res.status(400).json({ error: 'Invalid Service selected.' });

    const validQuantities = ['500 - 1,000', '1,000 - 5,000', '5,000 - 10,000', '10,000+'];
    if (!validQuantities.includes(quantity)) return res.status(400).json({ error: 'Invalid Quantity range selected.' });

    const validFrequencies = ['One-Time Requirement', 'Monthly Requirement', 'Quarterly Requirement', 'Long-Term Partnership'];
    if (!validFrequencies.includes(frequency)) return res.status(400).json({ error: 'Invalid Requirement frequency selected.' });

    // 7. Sanitization: Prevent XSS by escaping HTML tags in text values
    const cleanName = xss(name.trim());
    const cleanCompany = xss(company.trim());
    const cleanEmail = xss(email.trim());
    const cleanPhone = xss(phone.trim());
    const cleanCity = xss(city.trim());
    const cleanState = xss(state.trim());
    const cleanIndustry = xss(industry.trim());
    const cleanServiceType = xss(service_type.trim());
    const cleanBottleSize = bottle_size ? xss(bottle_size.trim()) : null;
    const cleanDesignReq = design_req ? xss(design_req.trim()) : null;
    const cleanQrReq = qr_req ? xss(qr_req.trim()) : null;
    const cleanDeliveryDate = delivery_date ? xss(delivery_date.trim()) : null;
    const cleanDeliveryLoc = delivery_loc ? xss(delivery_loc.trim()) : null;
    const cleanCampaignObj = campaign_obj ? xss(campaign_obj.trim()) : null;
    const cleanAdEvent = ad_event ? xss(ad_event.trim()) : null;
    const cleanAudience = audience ? xss(audience.trim()) : null;
    const cleanQuantity = xss(quantity.trim());
    const cleanFrequency = xss(frequency.trim());
    const cleanSource = source ? xss(source.trim()) : null;
    const cleanDetails = details ? xss(details.trim()) : null;

    // Calculate lead score (replicate current client logic for consistency)
    let leadScore = 0;
    if (cleanFrequency === 'Monthly Requirement' || cleanFrequency === 'Long-Term Partnership') leadScore += 5;
    if (cleanQuantity === '5,000 - 10,000' || cleanQuantity === '10,000+') leadScore += 3;

    // 8. Construct payload for database
    const payload = {
      name: cleanName,
      company: cleanCompany,
      email: cleanEmail,
      phone: cleanPhone,
      city: cleanCity,
      state: cleanState,
      industry: cleanIndustry,
      service_type: cleanServiceType,
      bottle_size: cleanBottleSize,
      design_req: cleanDesignReq,
      qr_req: cleanQrReq,
      delivery_date: cleanDeliveryDate,
      delivery_loc: cleanDeliveryLoc,
      campaign_obj: cleanCampaignObj,
      ad_event: cleanAdEvent,
      audience: cleanAudience,
      quantity: cleanQuantity,
      frequency: cleanFrequency,
      source: cleanSource,
      details: cleanDetails,
      timeline: "Not specified",
      lead_score: leadScore
    };

    // Store IP address if schema update has been run
    if (hasIpColumn) {
      payload.ip_address = ip;
    }

    // 9. Write to Supabase
    const { data: dbData, error: dbError } = await supabase
      .from('quotes')
      .insert([payload]);

    if (dbError) {
      console.error('Supabase write error:', dbError.message);
      // Return a clean generic error message without disclosing backend implementation details
      return res.status(500).json({ error: 'Database transaction failed. Please try again.' });
    }

    // 10. Success response
    return res.status(200).json({ success: true, message: 'Quote request submitted successfully.' });

  } catch (error) {
    console.error('Critical server error:', error);
    // Generic error response protecting backend stack details / debug logs
    return res.status(500).json({ error: 'Internal Server Error. Please contact support if the issue persists.' });
  }
};
