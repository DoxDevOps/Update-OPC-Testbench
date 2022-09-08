#!/bin/bash -l

#source ~/.bashrc
rvm use 2.5.3
#describe head -------------------------------------------
#git describe --tags > HEAD
rm -rf Gemfile.lock
#running bundle -------------------------------------------
bundle install --local

#running scripts and migration ----------------------------
#bin/update_art_metadata.sh development
bundle exec rake db:migrate
#rake db:migrate
mysql -uroot -proot openmrs < db/sql/openmrs_metadata_1_7.sql
mysql -uroot -proot openmrs < db/sql/moh_regimens_v2020.sql
mysql -uroot -proot openmrs < db/sql/bart2_views_schema_additions.sql
mysql -uroot -proot openmrs < db/sql/alternative_drug_names.sql

sudo /opt/nginx/sbin/nginx -s reload
#git describe --tags > HEAD

