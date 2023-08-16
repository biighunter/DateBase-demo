--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.4 (Ubuntu 15.4-1.pgdg22.10+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: biighunter
--

CREATE TABLE public.employee (
    em_id integer NOT NULL,
    full_name character varying(40),
    specialty character varying,
    age integer
);


ALTER TABLE public.employee OWNER TO biighunter;

--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: biighunter
--

COPY public.employee (em_id, full_name, specialty, age) FROM stdin;
4957	biighunter	nobody	22
3648	hussein hulk	HR	28
5712	farhad	CAO	34
3112	Esmaeil Ramnejad	DevOps Specialist	33
2741	edris	full stack	32
\.


--
-- Name: employee Employee_pkey; Type: CONSTRAINT; Schema: public; Owner: biighunter
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT "Employee_pkey" PRIMARY KEY (em_id);


--
-- PostgreSQL database dump complete
--

