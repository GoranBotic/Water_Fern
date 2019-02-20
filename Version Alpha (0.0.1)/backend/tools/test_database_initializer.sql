CREATE TABLE public.index
(
    submission_id integer NOT NULL,
    start_line integer NOT NULL,
    end_line integer NOT NULL,
    type character varying COLLATE pg_catalog."default" NOT NULL,
    index real[] NOT NULL,
    CONSTRAINT index_pkey PRIMARY KEY (submission_id, start_line, end_line, type),
    CONSTRAINT index_submission_id_fkey FOREIGN KEY (submission_id)
        REFERENCES public.submissions (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.index
    OWNER to postgres;

CREATE TABLE public.submissions
(
    id integer NOT NULL DEFAULT nextval('"submissions_ID_seq"'::regclass),
    data bytea,
    name character varying COLLATE pg_catalog."default",
    language character varying COLLATE pg_catalog."default",
    CONSTRAINT submissions_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.submissions
    OWNER to postgres;