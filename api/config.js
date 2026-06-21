module.exports = (req, res) => {
  // Prevent methods other than GET
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  // Use process.env.TURNSTILE_SITE_KEY, or fall back to Cloudflare's always-pass public test key
  const siteKey = process.env.TURNSTILE_SITE_KEY || '1x00000000000000000000AA';

  // Cache configuration response for 1 hour on the edge to maintain high performance
  res.setHeader('Cache-Control', 'public, max-age=3600, s-maxage=3600');
  res.setHeader('Content-Type', 'application/json');
  
  res.status(200).json({
    turnstileSiteKey: siteKey
  });
};
