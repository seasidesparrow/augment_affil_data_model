# augment_affil_data_model
Output record schema for the SciX/Honeycomb affiliation augmentation pipeline

## Description

This schema defines the output of the SciX Honeycomb Affiliation Augment 
pipeline, which takes input bib_data.affil metadata from an incoming ingested
model and outputs augmented affiliations (when possible).

Augmentations to affiliations include the following:

- `aff`: The raw affiliation string(s) for each author in the record (type: list)
- `aff_canonical`: Canonical affiliation strings for raw strings matched in our identifier database (type: list)
- `aff_abbrev`: Canonical abbreviations for the same (type: list)
- `aff_country`: Country of origin for matched strings (type: list)
- `aff_facet_hier`: Institution facet data used by the ADS and SciX user interfaces (type: list)
- `aff_id`: ADS Affiliation IDs for matched strings (type: list)
- `aff_iso_country`: ISO two-letter code for matched strings' country of origin (type: list)
- `author`: Normalized author names `(surname, given name)` (type: list)
- `bibcode`: The ADS Bibliographic Code for the record (type: string)
- `scix_id` The SciX Identifier for the record (type: string)

## Maintainer(s)

- Matthew Templeton, ADS @ Center for Astrophysics | Harvard & Smithsonian
