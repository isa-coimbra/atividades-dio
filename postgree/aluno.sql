CREATE TABLE aluno(
    id SERIAL,
        nome VARCHAR(255),
        cpf CHAR(11),
        observação TEXT,
        idade INTEGER,
        dinheiro NUMERIC(10,2),
        altura REAL,
        ativo BOOLEAN,
        data_nascimento DATE,
        hora_aula TIME,
        matriculado_em TIMESTAMP
);

SELECT * FROM aluno;

INSERT INTO aluno (
	nome,
	cpf,
	observação,
	idade,
	dinheiro,
	altura,
	ativo,
	data_nascimento,
	hora_aula,
	matriculado_em

) VALUES	(
	'Isabelle',
	'12345678900',
	'texto sobre o aluno',
	21,
	1200.50,
	1.70,
	TRUE,
	'2002-03-05',
	'17:30:00',
	'2023-03-31 10:29:00'
);


SELECT * 
FROM aluno 
WHERE id = 1

UPDATE aluno 
SET nome = 'Nico',
	cpf = '74125896321',
	observação = 'Novamente, isso é um teste',
	idade = 22,
	dinheiro = 14.20,
	altura = 1.75,
	ativo = FALSE,
	data_nascimento = '2001-03-31',
	hora_aula = '13:00:00',
	matriculado_em = '2023-04-26 08:56:00'
WHERE id = 1;


SELECT *
FROM aluno
WHERE nome= 'Nico';


DELETE 
FROM aluno
WHERE nome= 'Nico';






