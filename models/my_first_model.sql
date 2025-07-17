select
  "Software Name" as col1,
  "Status" as col2,
  "Owned" as col3,
  "Department" as col4,
  "Business Owner" as col5,
  "Tech Owner" as col6,
  "Support Type" as col7,
  NULL::text as col8,
  NULL::text as col9
from {{ ref('slm_data') }}

union all

select
  "Domain Name" as col1,
  "Status" as col2,
  NULL::text as col3,
  NULL::text as col4,
  NULL::text as col5,
  NULL::text as col6,
  NULL::text as col7,
  "TLD" as col8,
  "Lock" as col9
from {{ ref('phenom_domains') }}

union all

select
  "Display name" as col1,
  CASE WHEN "DirSyncEnabled" THEN 'Enabled' ELSE 'Disabled' END as col2,
  "User principal name" as col3,
  "Title" as col4,
  "Department" as col5,
  "City" as col6,
  "CountryOrRegion" as col7,
  "Office" as col8,
  "StateOrProvince" as col9
from {{ ref('data_365') }}
