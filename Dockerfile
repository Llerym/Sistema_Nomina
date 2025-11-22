# Use the official Odoo 18 image as base
# (confirmed available on Docker Hub: tags 18, 18.0, 18.0-YYYYMMDD) :contentReference[oaicite:0]{index=0}
FROM odoo:18.0

# Use root to create directories and change permissions
USER root

# Create directory for extra addons and data dir
RUN mkdir -p /mnt/extra-addons \
    && mkdir -p /var/lib/odoo \
    && chown -R odoo:odoo /mnt/extra-addons /var/lib/odoo

# Copy your custom modules into /mnt/extra-addons
# (these paths assume the folders are directly in the repo root)
COPY cinepolis_rrhh /mnt/extra-addons/cinepolis_rrhh
COPY om_hr_payroll /mnt/extra-addons/om_hr_payroll
COPY om_hr_payroll_account /mnt/extra-addons/om_hr_payroll_account

# Copy your Odoo configuration file
COPY odoo.conf /etc/odoo/odoo.conf
RUN chown odoo:odoo /etc/odoo/odoo.conf

# (Optional) If your custom modules need extra Python libraries:
# COPY requirements.txt /requirements.txt
# RUN pip install --no-cache-dir -r /requirements.txt

# Switch back to odoo user to run the service
USER odoo

# Expose the Odoo web port
EXPOSE 8069

# Default command: start Odoo with your config
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
