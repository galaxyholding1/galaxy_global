# Galaxy Global - Custom Frappe/ERPNext App

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Frappe](https://img.shields.io/badge/frappe-%3E%3D15.0-orange.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)

**Galaxy Global Group - Corporate ERP Layer**

Una aplicación personalizada de Frappe/ERPNext diseñada para gestionar la estructura corporativa completa del grupo empresarial Galaxy, que abarca múltiples jurisdicciones y líneas de negocio en EE.UU., Europa y otros territorios.

---

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Estructura del Grupo Galaxy](#-estructura-del-grupo-galaxy)
- [Arquitectura de la App](#-arquitectura-de-la-app)
- [Módulos](#-módulos)
- [DocTypes](#-doctypes)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Desarrollo](#-desarrollo)
- [Licencia](#-licencia)

---

## 🌟 Descripción General

Galaxy Global es una custom app de Frappe diseñada específicamente para gestionar:

- **Estructura corporativa multi-jurisdiccional** (USA, Luxemburgo, España, Malta, Estonia)
- **Operaciones industriales Bio** (8 plantas de producción en Castilla y León)
- **Finanzas y tesorería corporativa** (incluyendo Green Bonds e intercompany loans)
- **Plataformas Fintech** (Galaxy Pay Europa y USA-LATAM)
- **Seguros y garantías** (Sygma Insurance, Asterion)
- **Real Estate** (Galaxy Tower - arrendamiento de naves industriales)
- **Compliance y gestión de riesgos** regulatorios

---

## 🏢 Estructura del Grupo Galaxy

### Nivel 1: Matriz USA
- **Galaxy Global Corp Inc.** (Delaware)

### Nivel 2: Holding Luxemburgo
- **Luxembourg Holding S.A. (SOPARFI)**

### Nivel 3: Subsidiarias Operativas

#### España
- **Galaxy International Finance S.L.** (ETVE - Entidad de Tenencia de Valores Extranjeros)
- **Galaxy Bio Spain Holding S.L.** + 8 plantas industriales:
  - Galaxy Bio Burgos S.L.
  - Galaxy Bio Valladolid S.L.
  - Galaxy Bio Palencia S.L.
  - Galaxy Bio Zamora S.L.
  - Galaxy Bio Salamanca S.L.
  - Galaxy Bio León S.L.
  - Galaxy Bio Ávila S.L.
  - Galaxy Bio Segovia S.L.
- **Galaxy Financial Group S.L.**
- **Galaxy Tower Real Estate S.L.**

#### Malta
- **Sygma Insurance - Whiterock PCC Cell**

#### Europa (Estonia)
- **Galaxy Pay Europa OÜ** (Licencia PSD2)

#### USA
- **Galaxy Pay USA-LATAM LLC** (Delaware - Licencia MSB)
- **Galaxy Software & Data LLC** (Delaware)

---

## 🏗 Arquitectura de la App

```
galaxy_global/
├── galaxy_global/              # Carpeta principal de la app
│   ├── corporate_holding/      # Estructura legal y holding
│   ├── treasury_finance/       # Tesorería y finanzas
│   ├── bio_industrial/         # Plantas industriales Bio
│   ├── fintech_payments/       # Plataformas de pago
│   ├── insurance_guarantees/   # Seguros y garantías
│   ├── real_estate/            # Inmobiliario
│   ├── compliance_regulatory/  # Compliance y riesgos
│   ├── config/                 # Configuración
│   ├── public/                 # Assets públicos (CSS/JS)
│   └── templates/              # Templates HTML
├── __init__.py
├── hooks.py                    # Configuración de hooks
├── modules.txt                 # Lista de módulos
├── pyproject.toml              # Configuración Python (PEP 518)
├── setup.py                    # Setup tradicional
├── LICENSE                     # Licencia MIT
└── README.md                   # Este archivo
```

---

## 📦 Módulos

La aplicación está organizada en **7 módulos funcionales**:

### 1. **Corporate Holding** 🏛
Gestión de la estructura legal y corporativa del grupo.

**DocTypes:**
- Galaxy Legal Entity

### 2. **Treasury Finance** 💰
Gestión de tesorería, préstamos intercompany y bonos verdes.

**DocTypes:**
- Treasury Account
- Intercompany Loan
- Green Bond
- Green Bond Project (child table)

### 3. **Bio Industrial** 🏭
Gestión de plantas de producción de biocombustibles.

**DocTypes:**
- Bio Plant
- Certification

### 4. **Fintech Payments** 💳
Plataformas de pago Galaxy Pay (Europa y USA-LATAM).

**DocTypes:**
- Pay Platform
- Pay User Summary

### 5. **Insurance Guarantees** 🛡
Productos de seguros y facilidades de garantía (Sygma/Asterion).

**DocTypes:**
- Insurance Product
- Insurance Policy
- Guarantee Facility

### 6. **Real Estate** 🏢
Gestión de sitios industriales y contratos de arrendamiento.

**DocTypes:**
- Industrial Site
- Industrial Lease

### 7. **Compliance Regulatory** 📋
Licencias regulatorias, obligaciones y registro de riesgos.

**DocTypes:**
- Regulatory License
- Regulatory Obligation
- Risk Register

---

## 📝 DocTypes

### Corporate Holding

#### Galaxy Legal Entity
Representa cada entidad legal del grupo Galaxy.

**Campos principales:**
- `legal_name`: Nombre legal de la entidad
- `country`: País de registro
- `jurisdiction_type`: Tipo de jurisdicción (Delaware, SOPARFI, ETVE, etc.)
- `entity_role`: Rol en el grupo (Matriz, Holding, Operativa, etc.)
- `registration_number`: Número de registro
- `tax_id`: NIF/EIN/Tax ID
- `parent_entity`: Entidad padre (para jerarquía)

**Características:**
- Naming: Por `legal_name`
- Validación de referencias circulares en jerarquía
- Track changes habilitado

---

### Bio Industrial

#### Bio Plant
Gestiona las plantas industriales de producción.

**Campos principales:**
- `plant_name`: Nombre de la planta
- `legal_entity`: Entidad legal propietaria
- `location`: Ubicación/ciudad
- `capacity_tons_per_year`: Capacidad anual en toneladas
- `status`: Estado (Planning, Under Construction, Operational, etc.)
- `iscc_certificate`: Certificación ISCC
- `sicbios_certificate`: Certificación SICBIOS

**Características:**
- Naming: Por `plant_name`
- Links a certificaciones

#### Certification
Gestiona certificaciones (ISCC, SICBIOS, ESG, ISO, etc.).

**Campos principales:**
- `cert_type`: Tipo de certificación
- `holder_type`: Tipo de titular (Legal Entity o Bio Plant)
- `holder`: Titular (Dynamic Link)
- `issuer`: Emisor
- `issue_date` / `expiry_date`: Fechas de validez
- `is_active`: Estado activo

**Características:**
- Naming: Expression `{cert_type}-{holder}-{issue_date}`
- Auto-desactivación al expirar
- Alertas de expiración (30 días)

---

### Treasury Finance

#### Treasury Account
Cuentas bancarias del grupo.

**Campos principales:**
- `legal_entity`: Entidad propietaria
- `bank_name`: Nombre del banco
- `iban_or_account`: IBAN o número de cuenta
- `currency`: Moneda
- `is_pool_master`: Flag para cash pooling
- `swift_bic`: Código SWIFT/BIC

**Características:**
- Naming: Expression `{legal_entity}-{bank_name}-{currency}`

#### Intercompany Loan
Préstamos entre entidades del grupo.

**Campos principales:**
- `lender`: Entidad prestamista
- `borrower`: Entidad prestataria
- `principal_amount`: Monto principal
- `interest_rate`: Tasa de interés
- `loan_date` / `maturity_date`: Fechas del préstamo
- `outstanding_amount`: Saldo pendiente

**Características:**
- Validación: lender ≠ borrower
- Validación: maturity_date > loan_date
- Auto-inicialización de outstanding_amount

#### Green Bond
Bonos verdes emitidos por el grupo.

**Campos principales:**
- `bond_name`: Nombre del bono
- `issuer`: Entidad emisora
- `amount`: Monto emitido
- `coupon`: Tasa de cupón
- `issue_date` / `maturity_date`: Fechas
- `projects`: Tabla de proyectos financiados (child table)
- `total_allocated`: Total asignado (calculado)
- `total_co2_avoided`: CO2 evitado total (calculado)

**Características:**
- Child table: Green Bond Project
- Cálculo automático de totales
- Track changes habilitado

---

### Fintech Payments

#### Pay Platform
Plataformas de pago (Galaxy Pay Europa/USA-LATAM).

**Campos principales:**
- `platform_name`: Nombre de la plataforma
- `region`: Región (Europa, USA-LATAM)
- `legal_entity`: Entidad legal operadora
- `bank_partner`: Banco partner (Vodeno, Aion, Column, etc.)
- `api_base_url`: URL base del API
- `license_type`: Tipo de licencia (PSD2, MSB, AAI)

**Características:**
- Naming: Por `platform_name`

#### Pay User Summary
Resumen de usuarios y transacciones por plataforma.

**Campos principales:**
- `platform`: Plataforma
- `user_type`: Tipo (Retail, Business)
- `reporting_date`: Fecha de reporte
- `active_users`: Usuarios activos
- `monthly_tx_volume`: Volumen mensual de transacciones
- `average_tx_size`: Tamaño promedio (calculado)

**Características:**
- Cálculo automático de promedio

---

### Insurance Guarantees

#### Insurance Product
Productos de seguro ofrecidos.

**Campos principales:**
- `product_name`: Nombre del producto
- `product_type`: Tipo (Caución, Garantía, RC, D&O, Cyber, etc.)
- `coverage_description`: Descripción de cobertura

#### Insurance Policy
Pólizas de seguro emitidas.

**Campos principales:**
- `policy_number`: Número de póliza
- `product`: Producto de seguro
- `insured_entity`: Entidad asegurada
- `premium_amount`: Prima
- `sum_insured`: Suma asegurada
- `policy_start_date` / `policy_end_date`: Vigencia
- `status`: Estado (Draft, Issued, Active, Cancelled, etc.)

**Características:**
- Naming: Por `policy_number`
- Validación de fechas

#### Guarantee Facility
Facilidades de garantía (Asterion).

**Campos principales:**
- `client_entity`: Entidad cliente
- `limit_amount`: Límite de la facilidad
- `outstanding_amount`: Monto utilizado
- `facility_start_date` / `facility_end_date`: Vigencia

**Características:**
- Validación: outstanding ≤ limit

---

### Real Estate

#### Industrial Site
Sitios industriales y naves.

**Campos principales:**
- `site_name`: Nombre del sitio
- `legal_entity`: Entidad propietaria (Tower)
- `city` / `region` / `country`: Ubicación
- `surface_m2`: Superficie en m²
- `site_type`: Tipo (Industrial, Warehouse, Office, etc.)

**Características:**
- Naming: Por `site_name`

#### Industrial Lease
Contratos de arrendamiento de naves.

**Campos principales:**
- `site`: Sitio arrendado
- `tenant`: Entidad arrendataria
- `rent_amount`: Renta mensual/anual
- `start_date` / `end_date`: Vigencia
- `payment_frequency`: Frecuencia de pago

**Características:**
- Naming: Expression `LEASE-{site}-{tenant}-{####}`
- Validación de fechas

---

### Compliance Regulatory

#### Regulatory License
Licencias regulatorias del grupo.

**Campos principales:**
- `legal_entity`: Entidad titular
- `license_type`: Tipo (AAI, PSD2, MSB, Insurance, ETVE, etc.)
- `jurisdiction`: Jurisdicción
- `license_number`: Número de licencia
- `issue_date` / `expiry_date`: Vigencia
- `status`: Estado (Active, Suspended, Revoked, Expired)

**Características:**
- Auto-desactivación al expirar
- Alertas de expiración (60 días)

#### Regulatory Obligation
Obligaciones regulatorias periódicas.

**Campos principales:**
- `legal_entity`: Entidad obligada
- `regime`: Régimen regulatorio (GDPR, PSD2, AML, ETVE, etc.)
- `frequency`: Frecuencia (Monthly, Quarterly, Annually, etc.)
- `next_deadline`: Próximo vencimiento
- `responsible_person`: Responsable
- `status`: Estado (Pending, In Progress, Completed, Overdue)

**Características:**
- Auto-marcado como overdue
- Alertas de vencimiento (15 días)

#### Risk Register
Registro de riesgos corporativos.

**Campos principales:**
- `risk_title`: Título del riesgo
- `risk_category`: Categoría (Operational, Financial, Regulatory, IT/Cyber, etc.)
- `affected_entity`: Entidad afectada
- `probability`: Probabilidad (1-5)
- `impact`: Impacto (1-5)
- `risk_score`: Score (P × I, calculado)
- `owner_user`: Responsable
- `mitigation_plan`: Plan de mitigación

**Características:**
- Cálculo automático de risk score
- Color-coding: High (≥15), Medium (8-14), Low (<8)
- Validación: probability e impact entre 1-5

---

## 🚀 Instalación

### Prerrequisitos

- Frappe Framework >= 15.0
- Python >= 3.10
- Node.js >= 18
- MariaDB/PostgreSQL
- Redis

### Instalación usando Bench

```bash
# 1. Ir al directorio de Frappe bench
cd /path/to/frappe-bench

# 2. Clonar/copiar la app galaxy_global al directorio de apps
cp -r /home/ubuntu/galaxy_global apps/

# 3. Instalar la app en bench
bench get-app galaxy_global

# 4. Instalar la app en un sitio específico
bench --site your-site.local install-app galaxy_global

# 5. Migrar la base de datos
bench --site your-site.local migrate

# 6. Reiniciar bench
bench restart
```

### Instalación usando Docker (frappe_docker)

```bash
# 1. Copiar la app al directorio de apps del contenedor
docker cp /home/ubuntu/galaxy_global <container_name>:/home/frappe/frappe-bench/apps/

# 2. Entrar al contenedor
docker exec -it <container_name> bash

# 3. Instalar dependencias
cd /home/frappe/frappe-bench/apps/galaxy_global
pip install -e .

# 4. Instalar la app en el sitio
bench --site <site_name> install-app galaxy_global

# 5. Migrar
bench --site <site_name> migrate

# 6. Salir y reiniciar contenedores
exit
docker-compose restart
```

---

## ⚙️ Configuración

### Configuración Inicial

Después de instalar la app, sigue estos pasos:

#### 1. Crear Entidades Legales

Navega a: **Galaxy Global > Corporate Holding > Galaxy Legal Entity**

Crea las entidades en orden jerárquico:

1. **Galaxy Global Corp Inc.** (Matriz USA)
   - Country: United States
   - Jurisdiction: Delaware
   - Entity Role: Matriz

2. **Luxembourg Holding S.A.** (Holding)
   - Country: Luxembourg
   - Jurisdiction: SOPARFI Lux
   - Entity Role: Holding
   - Parent Entity: Galaxy Global Corp Inc.

3. Subsidiarias (España, Malta, Estonia, USA)...

#### 2. Configurar Plantas Bio

Navega a: **Galaxy Global > Bio Industrial > Bio Plant**

Crea las 8 plantas industriales de Castilla y León.

#### 3. Configurar Cuentas de Tesorería

Navega a: **Galaxy Global > Treasury Finance > Treasury Account**

Añade las cuentas bancarias de cada entidad.

#### 4. Configurar Plataformas de Pago

Navega a: **Galaxy Global > Fintech Payments > Pay Platform**

- Galaxy Pay Europa (Estonia - PSD2)
- Galaxy Pay USA-LATAM (Delaware - MSB)

#### 5. Cargar Licencias Regulatorias

Navega a: **Galaxy Global > Compliance Regulatory > Regulatory License**

Añade todas las licencias vigentes del grupo.

---

## 💻 Uso

### Casos de Uso Comunes

#### Emitir un Green Bond

1. Ir a **Treasury Finance > Green Bond**
2. Crear nuevo registro
3. Rellenar datos del bono (emisor, monto, cupón, fechas)
4. En la tabla "Projects", añadir plantas Bio financiadas
5. El sistema calculará automáticamente:
   - Total Allocated
   - Total CO2 Avoided
6. Guardar

#### Registrar un Préstamo Intercompany

1. Ir a **Treasury Finance > Intercompany Loan**
2. Crear nuevo registro
3. Seleccionar lender y borrower (entidades diferentes)
4. Ingresar monto, tasa, fechas
5. El sistema validará:
   - Lender ≠ Borrower
   - Maturity date > Loan date
6. Outstanding amount se inicializa automáticamente

#### Gestionar Certificaciones de Plantas

1. Ir a **Bio Industrial > Certification**
2. Crear nueva certificación
3. Seleccionar tipo (ISCC, SICBIOS, etc.)
4. Vincular a planta o entidad legal
5. El sistema alertará:
   - 30 días antes de expiración (amarillo)
   - Certificaciones expiradas (rojo)

#### Monitorear Riesgos

1. Ir a **Compliance Regulatory > Risk Register**
2. Crear nuevo riesgo
3. Asignar probabilidad (1-5) e impacto (1-5)
4. El sistema calculará automáticamente el Risk Score (P × I)
5. Dashboard mostrará:
   - Riesgo Alto (score ≥ 15): rojo
   - Riesgo Medio (score 8-14): amarillo
   - Riesgo Bajo (score < 8): verde

---

## 🛠 Desarrollo

### Estructura de un DocType

Cada DocType en la app tiene 3 archivos principales:

```
doctype_name/
├── doctype_name.json       # Definición del DocType
├── doctype_name.py         # Lógica del servidor (Python)
└── doctype_name.js         # Lógica del cliente (JavaScript)
```

### Añadir Nuevos Campos

Para añadir campos a un DocType existente:

1. Editar el archivo JSON del DocType
2. Añadir el nuevo campo en `fields` array
3. Actualizar `field_order`
4. Ejecutar: `bench --site <site> migrate`

### Añadir Validaciones Personalizadas

Editar el archivo `.py` del DocType:

```python
def validate(self):
    """Custom validation logic"""
    if self.some_field:
        # Your validation logic
        pass
```

### Añadir Lógica de Cliente

Editar el archivo `.js` del DocType:

```javascript
frappe.ui.form.on('DocType Name', {
    refresh: function(frm) {
        // Custom client-side logic
    }
});
```

### Testing

```bash
# Ejecutar tests
bench --site <site> run-tests --app galaxy_global

# Ejecutar tests de un módulo específico
bench --site <site> run-tests --app galaxy_global --module corporate_holding
```

### Exportar Fixtures

Para exportar DocTypes como fixtures:

```bash
# Editar hooks.py y añadir a fixtures
# Luego ejecutar:
bench --site <site> export-fixtures
```

---

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**.

```
MIT License

Copyright (c) 2025 Galaxy Global Group

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contacto y Soporte

**Galaxy DevOps Team**
- Email: devops@galaxynp.holdings
- Repository: https://github.com/GalaxyNP/galaxy-global-erpnext

---

## 🗺 Roadmap

### Fase 1 (Completada) ✅
- Estructura básica de la app
- 7 módulos funcionales
- 17 DocTypes principales
- Validaciones básicas

### Fase 2 (Próxima)
- [ ] Workflows de aprobación
- [ ] Dashboards personalizados por módulo
- [ ] Reports y analytics
- [ ] Integración con APIs externas
- [ ] Notificaciones automatizadas

### Fase 3 (Futuro)
- [ ] Portal de clientes para Galaxy Pay
- [ ] App móvil para inspecciones de plantas
- [ ] BI y predictive analytics
- [ ] Integración con blockchain para certificados

---

## 🙏 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📚 Recursos Adicionales

- [Frappe Framework Documentation](https://frappeframework.com/docs)
- [ERPNext Documentation](https://docs.erpnext.com/)
- [Frappe Developer Guide](https://frappeframework.com/docs/user/en/guides)

---

**Versión:** 0.0.1  
**Última actualización:** 13 de Diciembre, 2025  
**Autor:** Galaxy DevOps Team
