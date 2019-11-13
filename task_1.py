import psycopg2

try:
    conn = psycopg2.connect(dbname='ost', user='ost',
                            password='ost', host='localhost')

    cursor = conn.cursor()
    sql = """
    SELECT a.name, a.department, a.salary
    FROM public.employee a
    INNER JOIN
    (SELECT department, MAX(salary) AS salary
    FROM public.employee GROUP BY department) b
    ON a.department = b.department and a.salary = b.salary;"""

    cursor.execute(sql)

    for name, department, salary in cursor.fetchall():
        print(f'{name} from {department} recives the highest salary - {salary}')

except (Exception, psycopg2.Error) as error:
    print('Error while connecting to PostgreSQL', error)
finally:
    cursor.close()
    conn.close()
