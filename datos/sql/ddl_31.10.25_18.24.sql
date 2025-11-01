ALTER TABLE usuarios RENAME COLUMN tipo_suscripcion TO nivel_suscripcion;
ALTER TABLE usuarios DROP COLUMN habilitado;
ALTER TABLE recursos_digitales CHANGE COLUMN premium tipo_suscripcion VARCHAR(10) NOT NULL DEFAULT 'gratuita';
ALTER TABLE recursos_digitales RENAME COLUMN tipo_suscripcion TO nivel_suscripcion;