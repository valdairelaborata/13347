Plataforma de Cursos Online

Descritivo:
Uma API para gerenciar cursos online, alunos e matrículas. Permite cadastrar cursos, aulas e categorias, matricular alunos e acompanhar quais cursos cada aluno está cursando.

Entidades e Relacionamentos:
Aluno (id, nome, email)
Curso (id, titulo, descricao, categoria_id)
CategoriaCurso (id, nome)
Matrícula (id, aluno_id, curso_id, data_matricula)
Aula (id, curso_id, titulo, conteudo)

Funcionalidades:
CRUD de alunos, cursos, categorias e aulas.
Matricular alunos em cursos.
Listar cursos de um aluno e aulas de um curso.
Evitar matrícula duplicada no mesmo curso.
Filtrar cursos por categoria e status de matrícula.