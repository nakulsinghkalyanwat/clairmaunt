-- Supabase Schema Update
-- Run this query in the Supabase SQL Editor to remove logo and design columns from the quotes table.

ALTER TABLE quotes DROP COLUMN IF EXISTS logo_url;
ALTER TABLE quotes DROP COLUMN IF EXISTS design_url;
