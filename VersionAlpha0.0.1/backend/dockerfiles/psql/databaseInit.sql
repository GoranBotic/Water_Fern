DROP TABLE public.associations;
DROP TABLE public.index;
DROP TABLE public.submissions;


CREATE TABLE public.submissions
(
    id SERIAL NOT NULL,
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

CREATE TABLE public.index
(
    block_id SERIAL NOT NULL UNIQUE,
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


CREATE TABLE public.associations
(
    document1 integer NOT NULL, 
    document2 integer NOT NULL, 
    index1 integer NOT NULL, 
    index2 integer NOT NULL, 
    similarity real NOT NULL,
    CONSTRAINT doc1_id_key FOREIGN KEY (document1)
        REFERENCES public.submissions (id),
    CONSTRAINT doc2_id_key FOREIGN KEY (document2)
        REFERENCES public.submissions (id),
    CONSTRAINT index1_key FOREIGN KEY (index1)
        REFERENCES public.index (block_id),
    CONSTRAINT index2_key FOREIGN KEY (index2)
        REFERENCES public.index (block_id)
);

ALTER TABLE public.associations
    OWNER to postgres;