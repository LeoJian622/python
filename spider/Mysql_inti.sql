 CREATE  TABLE  question (
 	id INT AUTO_INCREMENT,
 	No VARCHAR(36) UNIQUE,
 	url VARCHAR(255),
 	title VARCHAR(255),
 	description TEXT,
 	input TEXT,
 	output TEXT,
 	prosampleinput TEXT,
 	prosampleoutput TEXT,
 	PRIMARY KEY(id),
 	);