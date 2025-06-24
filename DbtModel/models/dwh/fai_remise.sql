{{
    config( materialized='table' )
}}
with fai_remise as
(
    select
   cast(null as STRING) as id_client,
   cast(null as STRING) as id_marche,
   cast(null as DATE) as date_deb_cpv_marche,
   cast(null as DATE) as dt_fin_validite_remise,
   cast(null as DATE) as dt_deb_validite_remise,
   cast(null as STRING) as code_m,
   cast(null as STRING) as motif_maj,
   cast(null as FLOAT64) as id_cv, /* Relation to ref_condition_vente.id_cdv */
   cast(null as STRING) as user_maj,
   cast(null as STRING) as id_cible_marche,
   cast(null as FLOAT64) as qte_min,
   cast(null as FLOAT64) as id, /* Business key */
   cast(null as STRING) as statut,
   cast(null as FLOAT64) as qte_max,
   cast(null as FLOAT64) as palier,
   cast(null as NUMERIC) as tx_remise,
   cast(null as STRING) as canal_rdp,
   cast(null as STRING) as groupe_rdp,
   cast(null as DATE) as date_fin_cpv_marche,
   cast(null as DATE) as dt_maj
)
select *
from fai_remise
