# Galaxy Global - Guía de Instalación Rápida

## 🚀 Instalación en Frappe/ERPNext

### Método 1: Instalación con Bench (Recomendado)

```bash
# 1. Navegar al directorio de Frappe bench
cd /path/to/frappe-bench

# 2. Copiar la app galaxy_global al directorio de apps
cp -r /home/ubuntu/galaxy_global apps/galaxy_global

# 3. Instalar la app
bench get-app galaxy_global

# 4. Instalar en un sitio específico
bench --site tu-sitio.local install-app galaxy_global

# 5. Migrar la base de datos
bench --site tu-sitio.local migrate

# 6. Reiniciar
bench restart
```

### Método 2: Instalación con Docker

```bash
# 1. Copiar la app al contenedor
docker cp /home/ubuntu/galaxy_global frappe_docker_erpnext-python_1:/home/frappe/frappe-bench/apps/

# 2. Entrar al contenedor
docker exec -it frappe_docker_erpnext-python_1 bash

# 3. Instalar dependencias
cd /home/frappe/frappe-bench/apps/galaxy_global
pip install -e .

# 4. Instalar en sitio
bench --site galaxy-erp.localhost install-app galaxy_global

# 5. Migrar
bench --site galaxy-erp.localhost migrate

# 6. Salir y reiniciar
exit
docker-compose restart
```

## ✅ Verificación de Instalación

```bash
# Verificar que la app está instalada
bench --site tu-sitio.local list-apps

# Debería aparecer:
# frappe
# erpnext
# galaxy_global

# Verificar módulos
bench --site tu-sitio.local console
```

En la consola de Frappe:
```python
import frappe
frappe.get_all("Module Def", filters={"app_name": "galaxy_global"}, fields=["name"])
```

Deberías ver los 7 módulos:
- Corporate Holding
- Treasury Finance
- Bio Industrial
- Fintech Payments
- Insurance Guarantees
- Real Estate
- Compliance Regulatory

## 📋 Configuración Inicial

### Paso 1: Crear Entidades Legales

Ir a: **Galaxy Global > Corporate Holding > Galaxy Legal Entity**

Crear en orden jerárquico:

1. **Galaxy Global Corp Inc.**
   - Legal Name: Galaxy Global Corporation Inc.
   - Country: United States
   - Jurisdiction Type: Delaware
   - Entity Role: Matriz
   - Tax ID: [EIN number]

2. **Luxembourg Holding S.A.**
   - Legal Name: Luxembourg Holding S.A.
   - Country: Luxembourg
   - Jurisdiction Type: SOPARFI Lux
   - Entity Role: Holding
   - Parent Entity: Galaxy Global Corp Inc.
   - Tax ID: [Luxembourg tax number]

3. **Galaxy International Finance S.L.**
   - Legal Name: Galaxy International Finance S.L.
   - Country: Spain
   - Jurisdiction Type: ETVE
   - Entity Role: Financiera
   - Parent Entity: Luxembourg Holding S.A.
   - Tax ID: [NIF español]

... (continuar con las demás entidades)

### Paso 2: Configurar Plantas Bio

Ir a: **Galaxy Global > Bio Industrial > Bio Plant**

Ejemplo:
- Plant Name: Galaxy Bio Burgos
- Legal Entity: Galaxy Bio Burgos S.L.
- Location: Burgos
- Capacity (Tons/Year): 50000
- Status: Operational

### Paso 3: Configurar Tesorería

Ir a: **Galaxy Global > Treasury Finance > Treasury Account**

Ejemplo:
- Legal Entity: Galaxy Bio Spain Holding S.L.
- Bank Name: BBVA
- IBAN: ES00 1234 5678 9012 3456 7890
- Currency: EUR
- Is Pool Master: ☐

### Paso 4: Configurar Plataformas Pay

Ir a: **Galaxy Global > Fintech Payments > Pay Platform**

**Galaxy Pay Europa:**
- Platform Name: Galaxy Pay Europa
- Region: Europa
- Legal Entity: Galaxy Pay Europa OÜ
- Bank Partner: Vodeno
- License Type: PSD2
- Status: Active

**Galaxy Pay USA-LATAM:**
- Platform Name: Galaxy Pay USA-LATAM
- Region: USA-LATAM
- Legal Entity: Galaxy Pay USA-LATAM LLC
- Bank Partner: Column
- License Type: MSB
- Status: Active

## 🔍 Verificación de Funcionalidad

### Test 1: Crear una Entidad Legal
```python
import frappe

entity = frappe.get_doc({
    "doctype": "Galaxy Legal Entity",
    "legal_name": "Test Entity S.L.",
    "country": "Spain",
    "jurisdiction_type": "Spain SL",
    "entity_role": "Operativa",
    "tax_id": "B12345678"
})
entity.insert()
print(f"✓ Entity created: {entity.name}")
```

### Test 2: Crear una Planta Bio
```python
import frappe

plant = frappe.get_doc({
    "doctype": "Bio Plant",
    "plant_name": "Test Plant",
    "legal_entity": "Test Entity S.L.",
    "location": "Madrid",
    "capacity_tons_per_year": 10000,
    "status": "Planning"
})
plant.insert()
print(f"✓ Plant created: {plant.name}")
```

### Test 3: Crear un Green Bond
```python
import frappe

bond = frappe.get_doc({
    "doctype": "Green Bond",
    "bond_name": "Galaxy Green Bond 2025",
    "issuer": "Luxembourg Holding S.A.",
    "amount": 100000000,
    "currency": "EUR",
    "coupon": 3.5,
    "issue_date": "2025-01-15",
    "maturity_date": "2030-01-15",
    "status": "Issued"
})
bond.insert()
print(f"✓ Bond created: {bond.name}")
```

## 🛠 Troubleshooting

### Error: "App galaxy_global not found"
```bash
# Verificar que la app está en apps/
ls apps/galaxy_global

# Re-instalar
bench get-app galaxy_global
```

### Error: "DocType Galaxy Legal Entity not found"
```bash
# Ejecutar migración
bench --site tu-sitio.local migrate

# Clear cache
bench --site tu-sitio.local clear-cache
```

### Error: Permisos
```bash
# Dar permisos al usuario actual
bench --site tu-sitio.local set-admin-password [password]

# Verificar roles
bench --site tu-sitio.local add-system-manager [tu-email]
```

## 📞 Soporte

Si encuentras problemas:

1. Revisa los logs: `bench --site tu-sitio.local logs`
2. Consulta el README.md para más detalles
3. Contacta: devops@galaxynp.holdings

## 🎉 ¡Listo!

Tu instalación de Galaxy Global está completa. Accede a tu sitio y comienza a usar la aplicación:

- URL: http://tu-sitio.local (o tu dominio configurado)
- User: Administrator
- Password: [tu contraseña de admin]

Navega a **Galaxy Global** en el menú principal para ver todos los módulos disponibles.
