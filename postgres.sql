PGDMP     .    3                y           postgres     13.2 (Ubuntu 13.2-1.pgdg20.04+1)     13.2 (Ubuntu 13.2-1.pgdg20.04+1)     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    13452    postgres    DATABASE     ]   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';
    DROP DATABASE postgres;
                postgres    false            ?           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3001            ?            1259    24775 
   cidade_api    TABLE     N  CREATE TABLE public.cidade_api (
    id integer NOT NULL,
    nome character varying(50) NOT NULL,
    temperatura double precision NOT NULL,
    veloc_vent double precision NOT NULL,
    press double precision NOT NULL,
    humi double precision NOT NULL,
    longi character varying NOT NULL,
    lati character varying NOT NULL
);
    DROP TABLE public.cidade_api;
       public         heap    postgres    false            ?            1259    24773    cidade_api_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.cidade_api_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.cidade_api_id_seq;
       public          postgres    false    201            ?           0    0    cidade_api_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.cidade_api_id_seq OWNED BY public.cidade_api.id;
          public          postgres    false    200            -           2604    24778    cidade_api id    DEFAULT     n   ALTER TABLE ONLY public.cidade_api ALTER COLUMN id SET DEFAULT nextval('public.cidade_api_id_seq'::regclass);
 <   ALTER TABLE public.cidade_api ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            ?          0    24775 
   cidade_api 
   TABLE DATA           a   COPY public.cidade_api (id, nome, temperatura, veloc_vent, press, humi, longi, lati) FROM stdin;
    public          postgres    false    201   ?       ?           0    0    cidade_api_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.cidade_api_id_seq', 5, true);
          public          postgres    false    200            /           2606    24783    cidade_api cidade_api_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.cidade_api
    ADD CONSTRAINT cidade_api_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.cidade_api DROP CONSTRAINT cidade_api_pkey;
       public            postgres    false    201            ?   d   x?u?9?0D?z|,Ǳ(??4?
			??Y?t4?W???븠]f1??HHH?u,IR??׶???
????s]?\6De??????QU+hb"?W?s     