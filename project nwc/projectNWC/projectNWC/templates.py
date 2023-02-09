<!-- employee_list.html -->
{% for employee in employees %}
  <p>{{ employee.name }}</p>
  <p>{{ employee.email }}</p>
  <p>{{ employee.department }}</p>
{% endfor %}

