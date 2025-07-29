import requests

class EmployeeApi:
    """Класс для работы с API сотрудников"""

    def __init__(self, base_url):
        """Инициализация с базовым URL"""
        self.base_url = base_url

    def _send_request(self, method, endpoint, **kwargs):
        """Универсальный метод для отправки запросов"""
        url = f"{self.base_url}{endpoint}"
        try:
            resp = requests.request(method, url, **kwargs)
            resp.raise_for_status()  # Генерирует исключение при ошибке HTTP
            return resp.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Ошибка при запросе к API: {e}")

    def create_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active=True):
        """Создание нового сотрудника"""
        employee_data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }
        return self._send_request('POST', "/employee/create", json=employee_data)

    def get_employee(self, employee_id):
        """Получение информации о сотруднике по ID"""
        return self._send_request('GET', f"/employee/info/{employee_id}")

    def update_employee(self, employee_id, **kwargs):
        """Изменение данных сотрудника"""
        return self._send_request('PATCH', f"/employee/change/{employee_id}", json=kwargs)

