#!/bin/bash

echo "════════════════════════════════════════════════════════════"
echo "  GALAXY GLOBAL APP - SCRIPT DE VERIFICACIÓN"
echo "════════════════════════════════════════════════════════════"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0

# Function to check file
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $1"
    else
        echo -e "${RED}✗${NC} $1 ${RED}(MISSING)${NC}"
        ((ERRORS++))
    fi
}

# Function to check directory
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $1/"
    else
        echo -e "${RED}✗${NC} $1/ ${RED}(MISSING)${NC}"
        ((ERRORS++))
    fi
}

echo "1. Verificando archivos de configuración..."
echo "────────────────────────────────────────────────────────────"
check_file "__init__.py"
check_file "setup.py"
check_file "pyproject.toml"
check_file "LICENSE"
check_file "README.md"
check_file "INSTALLATION_GUIDE.md"
check_file "RESUMEN_EJECUTIVO.md"
check_file ".gitignore"
check_file "galaxy_global/__init__.py"
check_file "galaxy_global/hooks.py"
check_file "galaxy_global/modules.txt"
echo ""

echo "2. Verificando estructura de módulos..."
echo "────────────────────────────────────────────────────────────"
check_dir "galaxy_global/corporate_holding"
check_dir "galaxy_global/bio_industrial"
check_dir "galaxy_global/treasury_finance"
check_dir "galaxy_global/fintech_payments"
check_dir "galaxy_global/insurance_guarantees"
check_dir "galaxy_global/real_estate"
check_dir "galaxy_global/compliance_regulatory"
echo ""

echo "3. Verificando DocTypes (JSON)..."
echo "────────────────────────────────────────────────────────────"
check_file "galaxy_global/corporate_holding/doctype/galaxy_legal_entity/galaxy_legal_entity.json"
check_file "galaxy_global/bio_industrial/doctype/bio_plant/bio_plant.json"
check_file "galaxy_global/bio_industrial/doctype/certification/certification.json"
check_file "galaxy_global/treasury_finance/doctype/treasury_account/treasury_account.json"
check_file "galaxy_global/treasury_finance/doctype/intercompany_loan/intercompany_loan.json"
check_file "galaxy_global/treasury_finance/doctype/green_bond/green_bond.json"
check_file "galaxy_global/treasury_finance/doctype/green_bond_project/green_bond_project.json"
check_file "galaxy_global/fintech_payments/doctype/pay_platform/pay_platform.json"
check_file "galaxy_global/fintech_payments/doctype/pay_user_summary/pay_user_summary.json"
check_file "galaxy_global/insurance_guarantees/doctype/insurance_product/insurance_product.json"
check_file "galaxy_global/insurance_guarantees/doctype/insurance_policy/insurance_policy.json"
check_file "galaxy_global/insurance_guarantees/doctype/guarantee_facility/guarantee_facility.json"
check_file "galaxy_global/real_estate/doctype/industrial_site/industrial_site.json"
check_file "galaxy_global/real_estate/doctype/industrial_lease/industrial_lease.json"
check_file "galaxy_global/compliance_regulatory/doctype/regulatory_license/regulatory_license.json"
check_file "galaxy_global/compliance_regulatory/doctype/regulatory_obligation/regulatory_obligation.json"
check_file "galaxy_global/compliance_regulatory/doctype/risk_register/risk_register.json"
echo ""

echo "4. Contando archivos..."
echo "────────────────────────────────────────────────────────────"
json_count=$(find galaxy_global -name "*.json" -path "*/doctype/*" | wc -l)
py_count=$(find galaxy_global -name "*.py" -path "*/doctype/*" | wc -l)
js_count=$(find galaxy_global -name "*.js" -path "*/doctype/*" | wc -l)

echo "DocTypes (JSON): $json_count / 17"
echo "Python files: $py_count"
echo "JavaScript files: $js_count"
echo ""

echo "5. Verificando sintaxis JSON..."
echo "────────────────────────────────────────────────────────────"
JSON_ERRORS=0
for file in $(find galaxy_global -name "*.json" -path "*/doctype/*"); do
    if python3 -c "import json; json.load(open('$file'))" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $(basename $(dirname $file))"
    else
        echo -e "${RED}✗${NC} $(basename $(dirname $file)) ${RED}(SYNTAX ERROR)${NC}"
        ((JSON_ERRORS++))
    fi
done
echo ""

echo "════════════════════════════════════════════════════════════"
echo "  RESUMEN DE VERIFICACIÓN"
echo "════════════════════════════════════════════════════════════"
echo ""

if [ $ERRORS -eq 0 ] && [ $JSON_ERRORS -eq 0 ] && [ $json_count -eq 17 ]; then
    echo -e "${GREEN}✅ VERIFICACIÓN EXITOSA${NC}"
    echo ""
    echo "La app Galaxy Global está completa y lista para instalación."
    echo ""
    echo "Próximos pasos:"
    echo "1. Copiar a frappe-bench: cp -r . /path/to/frappe-bench/apps/galaxy_global"
    echo "2. Instalar app: bench get-app galaxy_global"
    echo "3. Instalar en sitio: bench --site <site> install-app galaxy_global"
    echo "4. Migrar: bench --site <site> migrate"
    echo ""
    echo "📖 Ver INSTALLATION_GUIDE.md para instrucciones detalladas"
    exit 0
else
    echo -e "${RED}❌ VERIFICACIÓN FALLIDA${NC}"
    echo ""
    echo "Errores encontrados:"
    echo "  - Archivos faltantes: $ERRORS"
    echo "  - Errores JSON: $JSON_ERRORS"
    echo "  - DocTypes esperados: 17, encontrados: $json_count"
    echo ""
    echo "Por favor revisa los errores arriba."
    exit 1
fi
