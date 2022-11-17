MariaDB soll installiert werden mit dem Password "Gu3487#2399!!+dj8v83bnd"

Die Datenbank soll "auth_register" heißen

es sollen die drei folgenden Tabellen erstellt werden:
	- admin_key_server(id, server_Id, pub_key, priv_key)
	- directory_server3(id, personal_ID, priv_key)
	- voters(id, PERSON_ID, HAS_VOTED, AUTH_ID)

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
CREATE TABLE admin_key_server (
	id BIGINT NOT NULL AUTO_INCREMENT, 
	server_id VARCHAR(1000),
	pub_key VARCHAR(1000),
	priv_key VARCHAR(1000),
	PRIMARY KEY (id));

CREATE TABLE directory_server3 (
	id BIGINT NOT NULL AUTO_INCREMENT,
	personal_ID VARCHAR(1000),
	priv_key VARCHAR(1000),
	PRIMARY KEY (id));

CREATE TABLE server (
	id BIGINT NOT NULL AUTO_INCREMENT,
	server_name VARCHAR(1000), 
	server_ip VARCHAR(100),
	server_port VARCHAR(100),
	PRIMARY KEY(id));

CREATE TABLE voters (
	id BIGINT NOT NULL AUTO_INCREMENT, 
	PERSON_ID VARCHAR(100) NOT NULL, 
	HAS_VOTED BOOLEAN, 
	AUTH_ID INT, 
	PRIMARY KEY (id) );

INSERT INTO voters(PERSON_ID,HAS_VOTED,AUTH_ID) VALUES ('T220101295', 0,347540), ('E530904263', 0,956856), ('U850101222', 0, 192493), ('V220403293', 0, 234843);
INSERT INTO server (server_name, server_ip, server_port) VALUES ('Loerrach','127.0.0.1','45677'),('Freiburg','127.0.0.1','45678'),('Hamburg','127.0.0.1','45679');

INSERT INTO admin_key_server (server_id) values ("default");


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

main.py: INITIAL RUN mit auskommentiertem Teil durchführen	
	

in der Tablle admin_key_server muss ein Insert ausgeführt werden:
	insert Admin Private Key

INSERT INTO admin_key_server (server_id) values ("default");


Link zu Video von Konzept in Miro: https://bwsyncandshare.kit.edu/s/K8XjXa5XmZC7YeH

Link zu Video von Realisierung des Projektes: https://bwsyncandshare.kit.edu/s/r99TsC2xGFfxo5p


########################################################################
Einfügen der ports aus mainx.py in die Servertabelle eintragen
########################################################################
mainx.py

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=45677, debug=True)




############################
Systeme (Container):
############################
Mariadb
register.py => Blockchain
main.py => Server1
main2.py => Server2
main3.py => Server3
                                                         

