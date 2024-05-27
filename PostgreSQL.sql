CREATE TABLE Students ( 
  student_id SERIAL PRIMARY KEY, 
  student_name VARCHAR(255) NOT NULL, 
  second_name VARCHAR(255) NOT NULL, 
  patronymic VARCHAR(255) NOT NULL, 
  university VARCHAR(255) NOT NULL, 
  study_profile VARCHAR(255) NOT NULL, 
  average_score VARCHAR(255) NOT NULL
);
INSERT INTO Students (student_name,  second_name, patronymic, university, study_profile, average_score) 
VALUES ('Ivan', 'Ivanov', 'Ivanovich', 'MSU', 'Mathematics', '4.5'),
('Anna', 'Petrova', 'Sergeevna', 'SPbSU', 'Physics', '4.7'),
('Olga', 'Sidorova', 'Alekseevna', 'HSE', 'Economics', '4.9'),
('Dmitry', 'Kuznetsov', 'Vladimirovich', 'MEPhI', 'Computer Science', '4.8'),
('Maria', 'Novikova', 'Pavlovna', 'MGIMO', 'International Relations', '4.6'),
('Alexey', 'Smirnov', 'Dmitrievich', 'MSU', 'Biology', '4.3'),
('Natalia', 'Fedorova', 'Igorevna', 'SPbSU', 'Chemistry', '4.4'),
('Elena', 'Morozova', 'Viktorovna', 'BMSTU', 'Engineering', '4.7'),
('Sergey', 'Vasiliev', 'Nikolaevich', 'HSE', 'Management', '4.5'),
('Andrey', 'Zakharov', 'Andreevich', 'RANEPA', 'Political Science', '4.6');
