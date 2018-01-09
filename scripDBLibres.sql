/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     8/1/2018 18:53:48                            */
/*==============================================================*/


drop table if exists HERRAMIENTA_OA;

drop table if exists MATERIA;

drop table if exists OBJETO_APRENDIJZAJE;

drop table if exists R5;

drop table if exists SOFTWARECREACIONOA;

drop table if exists TEMA;

drop table if exists USUARIO;

/*==============================================================*/
/* Table: HERRAMIENTA_OA                                        */
/*==============================================================*/
create table HERRAMIENTA_OA
(
   ID_HOA               int not null auto_increment,
   ID_S                 int,
   DESCRIPCION_HOA      varchar(30),
   NOMBRE_HOA           varchar(30),
   primary key (ID_HOA)
);

/*==============================================================*/
/* Table: MATERIA                                               */
/*==============================================================*/
create table MATERIA
(
   ID_M                 int not null auto_increment,
   NOMBRE_M             varchar(30),
   primary key (ID_M)
);

/*==============================================================*/
/* Table: OBJETO_APRENDIJZAJE                                   */
/*==============================================================*/
create table OBJETO_APRENDIJZAJE
(
   ID_OA                int not null auto_increment,
   ID_S                 int,
   ID_TEMA              int,
   ID_U                 int,
   TITULO               varchar(30),
   DESCRIPCION          varchar(100),
   RUTA                 varchar(100),
   FECHA_CREACION       date,
   PALABRAS_CLAVE       varchar(30),
   primary key (ID_OA)
);

/*==============================================================*/
/* Table: R5                                                    */
/*==============================================================*/
create table R5
(
   ID_M                 int not null,
   ID_TEMA              int not null,
   primary key (ID_M, ID_TEMA)
);

/*==============================================================*/
/* Table: SOFTWARECREACIONOA                                    */
/*==============================================================*/
create table SOFTWARECREACIONOA
(
   ID_S                 int not null auto_increment,
   TITULO_S             varchar(20),
   DESCRIPCION_S        varchar(40),
   primary key (ID_S)
);

/*==============================================================*/
/* Table: TEMA                                                  */
/*==============================================================*/
create table TEMA
(
   ID_TEMA              int not null auto_increment,
   TITULO               varchar(30),
   primary key (ID_TEMA)
);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
create table USUARIO
(
   NOMBRE               varchar(30),
   INSTITUCION          varchar(30),
   ID_U                 int not null auto_increment,
   primary key (ID_U)
);

alter table HERRAMIENTA_OA add constraint FK_R1 foreign key (ID_S)
      references SOFTWARECREACIONOA (ID_S) on delete restrict on update restrict;

alter table OBJETO_APRENDIJZAJE add constraint FK_R2 foreign key (ID_S)
      references SOFTWARECREACIONOA (ID_S) on delete restrict on update restrict;

alter table OBJETO_APRENDIJZAJE add constraint FK_R3 foreign key (ID_TEMA)
      references TEMA (ID_TEMA) on delete restrict on update restrict;

alter table OBJETO_APRENDIJZAJE add constraint FK_R4 foreign key (ID_U)
      references USUARIO (ID_U) on delete restrict on update restrict;

alter table R5 add constraint FK_R5 foreign key (ID_M)
      references MATERIA (ID_M) on delete restrict on update restrict;

alter table R5 add constraint FK_R6 foreign key (ID_TEMA)
      references TEMA (ID_TEMA) on delete restrict on update restrict;

