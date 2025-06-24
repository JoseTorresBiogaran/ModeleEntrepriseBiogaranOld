{{
    config( materialized='table' )
}}
with ref_condition_vente as
(
    select
   cast(null as DATE) as dt_maj,
   cast(null as STRING) as type_cdv,
   cast(null as STRING) as otc_engagement,
   cast(null as STRING) as otc_marque,
   cast(null as FLOAT64) as id_cdv, /* Business key */
   cast(null as STRING) as type_remise,
   cast(null as DATE) as dt_generation,
   cast(null as DATE) as dt_deb_cdv,
   cast(null as DATE) as dt_fin_cdv,
   cast(null as STRING) as user_maj,
   cast(null as STRING) as nom_cdv
)
select *
from ref_condition_vente
