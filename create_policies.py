import os
from datetime import datetime

# Dates
date_us = datetime.now().strftime("%B %d, %Y")
# Spanish date format
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
now = datetime.now()
date_es = f"{now.day} de {months[now.month-1]} de {now.year}"
date_jp = now.strftime("%Y年%m月%d日")

template_start = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="../assets/images/favicon-bg.png">
    <link rel="stylesheet" href="../style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Montserrat:wght@900&family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        .terms-content {{
            max-width: 800px;
            margin: 0 auto;
            color: var(--text-color);
        }}
        .terms-content h2 {{
            font-family: var(--font-heading);
            color: var(--accent-color);
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            text-transform: uppercase;
        }}
        .terms-content p {{
            margin-bottom: 15px;
            color: var(--text-muted);
            line-height: 1.6;
        }}
        .last-updated {{
            margin-bottom: 40px;
            color: var(--text-muted);
            font-style: italic;
        }}
        ul {{ list-style: disc; margin-left: 20px; margin-bottom: 15px; color: var(--text-muted); }}
        li {{ margin-bottom: 5px; }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container header-container">
            <div class="logo-container">
                <a href="index.html" style="text-decoration: none; display: flex; align-items: center; gap: 15px;">
                    <img src="../assets/images/racaille-logo.png" alt="Racaille Logo" class="logo-img">
                    <h1 class="logo-text">RACAILLE</h1>
                </a>
            </div>
            <button class="menu-toggle" aria-label="Open menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <nav class="nav-menu">
                <div class="nav-menu-wrapper">
                    <ul class="nav-links">
                        <li><a href="index.html#about">{nav_about}</a></li>
                        <li><a href="index.html#services">{nav_services}</a></li>
                        <li><a href="index.html#portfolio">{nav_portfolio}</a></li>
                        <li><a href="index.html#contact">{nav_contact}</a></li>
                        <li><a href="faq.html">FAQ</a></li>
                    </ul>
                    <div class="lang-switcher">
                        <button class="lang-btn {active_us}" onclick="setLang('US')">US</button>
                        <button class="lang-btn {active_es}" onclick="setLang('ES')">ES</button>
                        <button class="lang-btn {active_jp}" onclick="setLang('JP')">JP</button>
                    </div>
                </div>
            </nav>
        </div>
    </header>

    <section class="section">
        <div class="container">
            <h1 class="section-title">{page_title}</h1>
            <div class="terms-content">
                <p class="last-updated">{last_updated_label}: {date}</p>
                {content}
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 RACAILLE LLC. Built distinct.</p>
            <div style="margin-top: 20px; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">
                <a href="terms.html" style="color: var(--text-muted);">{link_terms}</a> |
                <a href="privacy.html" style="color: var(--text-muted);">{link_privacy}</a> |
                <a href="refund.html" style="color: var(--text-muted);">{link_refund}</a>
            </div>
            <div style="margin-top: 10px; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">
                <a href="https://www.designrush.com/agency/software-development/us" target="_blank" style="color: var(--text-muted);">{designrush_text}</a>
            </div>
        </div>
    </footer>

    <!-- Chat Widget -->
    <div class="racaille-chat-widget">
        <div class="chat-trigger">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        </div>
        <div class="chat-options">
            <a href="https://m.me/racaille.llc" target="_blank" class="chat-btn messenger" title="Messenger">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2C6.48 2 2 6.03 2 11c0 2.87 1.43 5.43 3.75 7.05V22l3.43-1.88c.91.25 1.87.38 2.82.38 5.52 0 10-4.03 10-9S17.52 2 12 2zm1.14 11.83L10.3 11l-3.24 3.48 3.56-3.83 2.84 2.83 3.24-3.48-3.56 3.83z"/></svg>
            </a>
            <a href="https://ig.me/m/racaille.llc" target="_blank" class="chat-btn instagram" title="Instagram">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
            </a>
            <a href="https://wa.me/16462616526" target="_blank" class="chat-btn whatsapp" title="WhatsApp">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
            </a>
        </div>
    </div>

    <script>
        function setLang(lang) {{
            document.cookie = "racaille_lang=" + lang + "; path=/; max-age=31536000";
            window.location.href = "../" + lang + "/";
        }}
        document.querySelector(".menu-toggle").addEventListener("click", function() {{
            document.querySelector(".nav-menu").classList.toggle("active");
            this.classList.toggle("active");
        }});
        document.querySelectorAll(".nav-links a").forEach(link => {{
            link.addEventListener("click", () => {{
                document.querySelector(".nav-menu").classList.remove("active");
                document.querySelector(".menu-toggle").classList.remove("active");
            }});
        }});
        const chatWidget = document.querySelector(".racaille-chat-widget");
        document.querySelector(".chat-trigger").addEventListener("click", function(e) {{
            e.stopPropagation();
            chatWidget.classList.toggle("active");
        }});
        document.addEventListener("click", function(e) {{
            if (!chatWidget.contains(e.target)) {{
                chatWidget.classList.remove("active");
            }}
        }});
    </script>
</body>
</html>"""

# Privacy Content
privacy_content_us = """
<p>Racaille LLC ("Racaille", "we", "our", or "us") is committed to protecting the privacy of visitors, clients, and partners who access our corporate website racaille.space.</p>
<p>This Privacy Policy explains how we collect, use, store, and protect personal information.</p>

<h2>1. Information We Collect</h2>
<p>We may collect the following types of information:</p>
<p><strong>a. Information You Provide Voluntarily</strong></p>
<ul>
    <li>Full name</li>
    <li>Email address</li>
    <li>Phone number</li>
    <li>Company or business information</li>
    <li>Any information submitted through contact forms or direct communications</li>
</ul>
<p><strong>b. Automatically Collected Information</strong></p>
<ul>
    <li>IP address</li>
    <li>Browser type and device information</li>
    <li>Pages visited and interaction data</li>
    <li>Date and time of access</li>
</ul>
<p>This data is collected for security, analytics, and service improvement purposes.</p>

<h2>2. How We Use Information</h2>
<p>Collected information may be used to:</p>
<ul>
    <li>Respond to inquiries and business communications</li>
    <li>Provide information about our services</li>
    <li>Improve website performance and user experience</li>
    <li>Maintain security and prevent fraud</li>
    <li>Comply with legal and regulatory obligations</li>
</ul>
<p>We do not use personal data for unsolicited marketing.</p>

<h2>3. Data Sharing & Disclosure</h2>
<p>Racaille LLC does not sell, rent, or trade personal information.</p>
<p>Information may be shared only with:</p>
<ul>
    <li>Trusted service providers necessary to operate the website</li>
    <li>Legal or regulatory authorities when required by law</li>
</ul>
<p>All third parties are required to maintain confidentiality and data protection standards.</p>

<h2>4. Data Security</h2>
<p>We implement appropriate technical and organizational security measures to protect personal data from:</p>
<ul>
    <li>Unauthorized access</li>
    <li>Disclosure</li>
    <li>Alteration</li>
    <li>Destruction</li>
</ul>
<p>However, no internet transmission is 100% secure, and absolute security cannot be guaranteed.</p>

<h2>5. Data Retention</h2>
<p>Personal data is retained only as long as necessary to:</p>
<ul>
    <li>Fulfill the purposes outlined in this policy</li>
    <li>Comply with legal or contractual obligations</li>
</ul>

<h2>6. Your Rights</h2>
<p>Depending on your jurisdiction, you may have the right to:</p>
<ul>
    <li>Request access to your personal data</li>
    <li>Request correction or deletion</li>
    <li>Object to certain data processing activities</li>
</ul>
<p>Requests can be submitted using the contact information below.</p>

<h2>7. Contact Information</h2>
<p>For privacy-related inquiries, please contact:</p>
<p>Email: contact@racaille.space</p>
<p>Company: Racaille LLC<br>Website: https://racaille.space</p>
"""

# Refund Content
refund_content_us = """
<p>Racaille.space is the corporate website of Racaille LLC, used to present company information, services, and business offerings.</p>

<h2>1. Nature of Services</h2>
<p>Racaille LLC provides:</p>
<ul>
    <li>Software development services</li>
    <li>Business automation solutions</li>
    <li>Digital platforms and consulting services</li>
</ul>
<p>No physical goods are sold through this website.</p>

<h2>2. Payments & Contracts</h2>
<p>Payments for services offered by Racaille LLC:</p>
<ul>
    <li>Are handled only after direct agreement with the client</li>
    <li>May require signed contracts, proposals, or service agreements</li>
    <li>Are not processed automatically through racaille.space</li>
</ul>
<p>Any payment terms are defined individually per project or service.</p>

<h2>3. Refund Policy</h2>
<p>Because Racaille LLC provides custom digital services, refunds are subject to the terms defined in the specific service agreement or contract.</p>
<p>Unless otherwise stated in writing:</p>
<ul>
    <li>Deposits and completed service milestones are non-refundable</li>
</ul>
<p>Refunds may be considered only in cases of:</p>
<ul>
    <li>Duplicate payments</li>
    <li>Proven billing errors</li>
    <li>Services not initiated due to fault exclusively attributable to Racaille LLC</li>
</ul>
<p>All refund requests are reviewed on a case-by-case basis.</p>

<h2>4. Cancellations</h2>
<p>Service cancellations:</p>
<ul>
    <li>Must be requested in writing</li>
    <li>Do not automatically entitle the client to a refund</li>
    <li>Do not affect completed or delivered work</li>
</ul>

<h2>5. Chargebacks</h2>
<p>Unauthorized chargebacks without prior communication may result in:</p>
<ul>
    <li>Suspension of services</li>
    <li>Termination of business relationship</li>
</ul>
<p>Clients are encouraged to contact Racaille LLC first to resolve any billing concerns.</p>

<h2>6. Contact Information</h2>
<p>All billing, refund, or service-related inquiries must be directed to:</p>
<p>Email: contact@racaille.space</p>
<p>Company: Racaille LLC</p>
"""

# Translations (Simplified for script brevity, but in real scenario would be full text)
# ... Actually I will construct them fully to ensure quality.

privacy_content_es = privacy_content_us.replace("Racaille LLC (\"Racaille\", \"we\", \"our\", or \"us\") is committed to protecting the privacy of visitors, clients, and partners who access our corporate website racaille.space.", "Racaille LLC (\"Racaille\", \"nosotros\" o \"nuestro\") se compromete a proteger la privacidad de los visitantes, clientes y socios que acceden a nuestro sitio web corporativo racaille.space.")
privacy_content_es = privacy_content_es.replace("This Privacy Policy explains how we collect, use, store, and protect personal information.", "Esta Política de Privacidad explica cómo recopilamos, utilizamos, almacenamos y protegemos la información personal.")
privacy_content_es = privacy_content_es.replace("1. Information We Collect", "1. Información que Recopilamos")
privacy_content_es = privacy_content_es.replace("We may collect the following types of information:", "Podemos recopilar los siguientes tipos de información:")
privacy_content_es = privacy_content_es.replace("a. Information You Provide Voluntarily", "a. Información que Usted Proporciona Voluntariamente")
privacy_content_es = privacy_content_es.replace("Full name", "Nombre completo").replace("Email address", "Dirección de correo electrónico").replace("Phone number", "Número de teléfono").replace("Company or business information", "Información de la empresa o negocio").replace("Any information submitted through contact forms or direct communications", "Cualquier información enviada a través de formularios de contacto o comunicaciones directas")
privacy_content_es = privacy_content_es.replace("b. Automatically Collected Information", "b. Información Recopilada Automáticamente")
privacy_content_es = privacy_content_es.replace("IP address", "Dirección IP").replace("Browser type and device information", "Tipo de navegador e información del dispositivo").replace("Pages visited and interaction data", "Páginas visitadas y datos de interacción").replace("Date and time of access", "Fecha y hora de acceso")
privacy_content_es = privacy_content_es.replace("This data is collected for security, analytics, and service improvement purposes.", "Estos datos se recopilan con fines de seguridad, análisis y mejora del servicio.")
privacy_content_es = privacy_content_es.replace("2. How We Use Information", "2. Cómo Usamos la Información")
privacy_content_es = privacy_content_es.replace("Collected information may be used to:", "La información recopilada puede utilizarse para:")
privacy_content_es = privacy_content_es.replace("Respond to inquiries and business communications", "Responder a consultas y comunicaciones comerciales").replace("Provide information about our services", "Proporcionar información sobre nuestros servicios").replace("Improve website performance and user experience", "Mejorar el rendimiento del sitio web y la experiencia del usuario").replace("Maintain security and prevent fraud", "Mantener la seguridad y prevenir el fraude").replace("Comply with legal and regulatory obligations", "Cumplir con obligaciones legales y reglamentarias")
privacy_content_es = privacy_content_es.replace("We do not use personal data for unsolicited marketing.", "No utilizamos datos personales para marketing no solicitado.")
privacy_content_es = privacy_content_es.replace("3. Data Sharing & Disclosure", "3. Intercambio y Divulgación de Datos")
privacy_content_es = privacy_content_es.replace("Racaille LLC does not sell, rent, or trade personal information.", "Racaille LLC no vende, alquila ni comercializa información personal.")
privacy_content_es = privacy_content_es.replace("Information may be shared only with:", "La información solo se puede compartir con:")
privacy_content_es = privacy_content_es.replace("Trusted service providers necessary to operate the website", "Proveedores de servicios de confianza necesarios para operar el sitio web").replace("Legal or regulatory authorities when required by law", "Autoridades legales o reguladoras cuando lo requiera la ley")
privacy_content_es = privacy_content_es.replace("All third parties are required to maintain confidentiality and data protection standards.", "Se exige a todos los terceros que mantengan la confidencialidad y los estándares de protección de datos.")
privacy_content_es = privacy_content_es.replace("4. Data Security", "4. Seguridad de los Datos")
privacy_content_es = privacy_content_es.replace("We implement appropriate technical and organizational security measures to protect personal data from:", "Implementamos medidas de seguridad técnicas y organizativas adecuadas para proteger los datos personales contra:")
privacy_content_es = privacy_content_es.replace("Unauthorized access", "Acceso no autorizado").replace("Disclosure", "Divulgación").replace("Alteration", "Alteración").replace("Destruction", "Destrucción")
privacy_content_es = privacy_content_es.replace("However, no internet transmission is 100% secure, and absolute security cannot be guaranteed.", "Sin embargo, ninguna transmisión por Internet es 100% segura y no se puede garantizar una seguridad absoluta.")
privacy_content_es = privacy_content_es.replace("5. Data Retention", "5. Retención de Datos")
privacy_content_es = privacy_content_es.replace("Personal data is retained only as long as necessary to:", "Los datos personales se conservan solo el tiempo necesario para:")
privacy_content_es = privacy_content_es.replace("Fulfill the purposes outlined in this policy", "Cumplir con los fines descritos en esta política").replace("Comply with legal or contractual obligations", "Cumplir con obligaciones legales o contractuales")
privacy_content_es = privacy_content_es.replace("6. Your Rights", "6. Sus Derechos")
privacy_content_es = privacy_content_es.replace("Depending on your jurisdiction, you may have the right to:", "Dependiendo de su jurisdicción, puede tener derecho a:")
privacy_content_es = privacy_content_es.replace("Request access to your personal data", "Solicitar acceso a sus datos personales").replace("Request correction or deletion", "Solicitar corrección o eliminación").replace("Object to certain data processing activities", "Oponerse a ciertas actividades de procesamiento de datos")
privacy_content_es = privacy_content_es.replace("Requests can be submitted using the contact information below.", "Las solicitudes se pueden enviar utilizando la información de contacto a continuación.")
privacy_content_es = privacy_content_es.replace("7. Contact Information", "7. Información de Contacto")
privacy_content_es = privacy_content_es.replace("For privacy-related inquiries, please contact:", "Para consultas relacionadas con la privacidad, comuníquese con:")

refund_content_es = refund_content_us.replace("Racaille.space is the corporate website of Racaille LLC, used to present company information, services, and business offerings.", "Racaille.space es el sitio web corporativo de Racaille LLC, utilizado para presentar información de la empresa, servicios y ofertas comerciales.")
refund_content_es = refund_content_es.replace("1. Nature of Services", "1. Naturaleza de los Servicios")
refund_content_es = refund_content_es.replace("Racaille LLC provides:", "Racaille LLC proporciona:")
refund_content_es = refund_content_es.replace("Software development services", "Servicios de desarrollo de software").replace("Business automation solutions", "Soluciones de automatización empresarial").replace("Digital platforms and consulting services", "Plataformas digitales y servicios de consultoría")
refund_content_es = refund_content_es.replace("No physical goods are sold through this website.", "No se venden bienes físicos a través de este sitio web.")
refund_content_es = refund_content_es.replace("2. Payments & Contracts", "2. Pagos y Contratos")
refund_content_es = refund_content_es.replace("Payments for services offered by Racaille LLC:", "Los pagos por los servicios ofrecidos por Racaille LLC:")
refund_content_es = refund_content_es.replace("Are handled only after direct agreement with the client", "Se manejan solo después de un acuerdo directo con el cliente").replace("May require signed contracts, proposals, or service agreements", "Pueden requerir contratos firmados, propuestas o acuerdos de servicio").replace("Are not processed automatically through racaille.space", "No se procesan automáticamente a través de racaille.space")
refund_content_es = refund_content_es.replace("Any payment terms are defined individually per project or service.", "Cualquier condición de pago se define individualmente por proyecto o servicio.")
refund_content_es = refund_content_es.replace("3. Refund Policy", "3. Política de Reembolso")
refund_content_es = refund_content_es.replace("Because Racaille LLC provides custom digital services, refunds are subject to the terms defined in the specific service agreement or contract.", "Debido a que Racaille LLC proporciona servicios digitales personalizados, los reembolsos están sujetos a los términos definidos en el acuerdo de servicio o contrato específico.")
refund_content_es = refund_content_es.replace("Unless otherwise stated in writing:", "A menos que se indique lo contrario por escrito:")
refund_content_es = refund_content_es.replace("Deposits and completed service milestones are non-refundable", "Los depósitos y los hitos de servicio completados no son reembolsables")
refund_content_es = refund_content_es.replace("Refunds may be considered only in cases of:", "Los reembolsos pueden considerarse solo en casos de:")
refund_content_es = refund_content_es.replace("Duplicate payments", "Pagos duplicados").replace("Proven billing errors", "Errores de facturación comprobados").replace("Services not initiated due to fault exclusively attributable to Racaille LLC", "Servicios no iniciados por culpa atribuible exclusivamente a Racaille LLC")
refund_content_es = refund_content_es.replace("All refund requests are reviewed on a case-by-case basis.", "Todas las solicitudes de reembolso se revisan caso por caso.")
refund_content_es = refund_content_es.replace("4. Cancellations", "4. Cancelaciones")
refund_content_es = refund_content_es.replace("Service cancellations:", "Cancelaciones de servicios:")
refund_content_es = refund_content_es.replace("Must be requested in writing", "Deben solicitarse por escrito").replace("Do not automatically entitle the client to a refund", "No dan derecho automáticamente al cliente a un reembolso").replace("Do not affect completed or delivered work", "No afectan el trabajo completado o entregado")
refund_content_es = refund_content_es.replace("5. Chargebacks", "5. Contracargos")
refund_content_es = refund_content_es.replace("Unauthorized chargebacks without prior communication may result in:", "Los contracargos no autorizados sin comunicación previa pueden resultar en:")
refund_content_es = refund_content_es.replace("Suspension of services", "Suspensión de servicios").replace("Termination of business relationship", "Terminación de la relación comercial")
refund_content_es = refund_content_es.replace("Clients are encouraged to contact Racaille LLC first to resolve any billing concerns.", "Se recomienda a los clientes que se comuniquen primero con Racaille LLC para resolver cualquier inquietud de facturación.")
refund_content_es = refund_content_es.replace("6. Contact Information", "6. Información de Contacto")
refund_content_es = refund_content_es.replace("All billing, refund, or service-related inquiries must be directed to:", "Todas las consultas relacionadas con facturación, reembolsos o servicios deben dirigirse a:")

# Japanese (Rough translation, keeping English terms where appropriate for clarity or simplicity in this context)
privacy_content_jp = """
<p>Racaille LLC（以下「Racaille」、「当社」）は、当社の企業ウェブサイトracaille.spaceにアクセスする訪問者、クライアント、およびパートナーのプライバシーを保護することをお約束します。</p>
<p>このプライバシーポリシーでは、個人情報の収集、使用、保存、および保護の方法について説明します。</p>

<h2>1. 収集する情報</h2>
<p>当社は、以下の種類の情報を収集する場合があります：</p>
<p><strong>a. 自発的に提供される情報</strong></p>
<ul>
    <li>氏名</li>
    <li>メールアドレス</li>
    <li>電話番号</li>
    <li>会社またはビジネス情報</li>
    <li>お問い合わせフォームまたは直接の連絡を通じて送信された情報</li>
</ul>
<p><strong>b. 自動的に収集される情報</strong></p>
<ul>
    <li>IPアドレス</li>
    <li>ブラウザの種類とデバイス情報</li>
    <li>訪問ページとインタラクションデータ</li>
    <li>アクセス日時</li>
</ul>
<p>このデータは、セキュリティ、分析、およびサービス向上の目的で収集されます。</p>

<h2>2. 情報の使用方法</h2>
<p>収集された情報は、以下の目的で使用される場合があります：</p>
<ul>
    <li>お問い合わせやビジネスコミュニケーションへの対応</li>
    <li>サービスに関する情報の提供</li>
    <li>ウェブサイトのパフォーマンスとユーザーエクスペリエンスの向上</li>
    <li>セキュリティの維持と不正防止</li>
    <li>法的および規制上の義務の遵守</li>
</ul>
<p>当社は、個人情報を未承諾のマーケティングに使用することはありません。</p>

<h2>3. データの共有と開示</h2>
<p>Racaille LLCは、個人情報を販売、貸与、または取引することはありません。</p>
<p>情報は、以下の場合にのみ共有されることがあります：</p>
<ul>
    <li>ウェブサイトの運営に必要な信頼できるサービスプロバイダー</li>
    <li>法律により要求される場合の法的または規制当局</li>
</ul>
<p>すべての第三者は、機密保持およびデータ保護基準を維持することが求められます。</p>

<h2>4. データセキュリティ</h2>
<p>当社は、個人情報を以下から保護するために適切な技術的および組織的なセキュリティ対策を講じています：</p>
<ul>
    <li>不正アクセス</li>
    <li>開示</li>
    <li>改ざん</li>
    <li>破壊</li>
</ul>
<p>ただし、インターネット送信は100％安全ではなく、絶対的なセキュリティを保証することはできません。</p>

<h2>5. データ保持</h2>
<p>個人データは、以下の目的のために必要な期間のみ保持されます：</p>
<ul>
    <li>本ポリシーに記載された目的の達成</li>
    <li>法的または契約上の義務の遵守</li>
</ul>

<h2>6. お客様の権利</h2>
<p>管轄区域によっては、以下の権利がある場合があります：</p>
<ul>
    <li>個人データへのアクセス要求</li>
    <li>訂正または削除の要求</li>
    <li>特定のデータ処理活動への異議申し立て</li>
</ul>
<p>リクエストは、以下の連絡先情報を使用して送信できます。</p>

<h2>7. お問い合わせ</h2>
<p>プライバシーに関するお問い合わせは、以下までご連絡ください：</p>
<p>メール: contact@racaille.space</p>
<p>会社名: Racaille LLC<br>ウェブサイト: https://racaille.space</p>
"""

refund_content_jp = """
<p>Racaille.spaceは、Racaille LLCの企業ウェブサイトであり、会社情報、サービス、およびビジネスオファリングを提示するために使用されます。</p>

<h2>1. サービスの性質</h2>
<p>Racaille LLCは以下を提供します：</p>
<ul>
    <li>ソフトウェア開発サービス</li>
    <li>ビジネス自動化ソリューション</li>
    <li>デジタルプラットフォームおよびコンサルティングサービス</li>
</ul>
<p>このウェブサイトを通じて物理的な商品は販売されません。</p>

<h2>2. 支払いと契約</h2>
<p>Racaille LLCが提供するサービスの支払い：</p>
<ul>
    <li>クライアントとの直接の合意後にのみ処理されます</li>
    <li>署名された契約書、提案書、またはサービス契約が必要な場合があります</li>
    <li>racaille.spaceを通じて自動的に処理されることはありません</li>
</ul>
<p>支払い条件は、プロジェクトまたはサービスごとに個別に定義されます。</p>

<h2>3. 返金ポリシー</h2>
<p>Racaille LLCはカスタムデジタルサービスを提供するため、返金は特定のサービス契約または契約書で定義された条件に従います。</p>
<p>書面で別段の記載がない限り：</p>
<ul>
    <li>デポジットおよび完了したサービスマイルストーンは返金不可です</li>
</ul>
<p>返金は、以下の場合にのみ検討される場合があります：</p>
<ul>
    <li>重複支払い</li>
    <li>証明された請求エラー</li>
    <li>Racaille LLCに専ら起因する過失によりサービスが開始されなかった場合</li>
</ul>
<p>すべての返金リクエストは、ケースバイケースで審査されます。</p>

<h2>4. キャンセル</h2>
<p>サービスのキャンセル：</p>
<ul>
    <li>書面でリクエストする必要があります</li>
    <li>自動的にクライアントに返金の権利を与えるものではありません</li>
    <li>完了した作業または納品された作業には影響しません</li>
</ul>

<h2>5. チャージバック</h2>
<p>事前の連絡なしに行われた不正なチャージバックは、以下をもたらす可能性があります：</p>
<ul>
    <li>サービスの停止</li>
    <li>取引関係の終了</li>
</ul>
<p>クライアントは、請求に関する懸念を解決するために、まずRacaille LLCに連絡することをお勧めします。</p>

<h2>6. お問い合わせ</h2>
<p>すべての請求、返金、またはサービスに関するお問い合わせは、以下までご連絡ください：</p>
<p>メール: contact@racaille.space</p>
<p>会社名: Racaille LLC</p>
"""

def create_file(path, content, title, lang, active_lang, nav_text, footer_links, designrush_text):
    nav_about, nav_services, nav_portfolio, nav_contact = nav_text
    link_terms, link_privacy, link_refund = footer_links
    active_us = "active" if active_lang == "US" else ""
    active_es = "active" if active_lang == "ES" else ""
    active_jp = "active" if active_lang == "JP" else ""

    last_updated_label = "Last updated"
    if lang == "es": last_updated_label = "Última actualización"
    if lang == "ja": last_updated_label = "最終更新日"

    date = date_us
    if lang == "es": date = date_es
    if lang == "ja": date = date_jp

    html = template_start.format(
        lang=lang,
        title=title,
        nav_about=nav_about,
        nav_services=nav_services,
        nav_portfolio=nav_portfolio,
        nav_contact=nav_contact,
        active_us=active_us,
        active_es=active_es,
        active_jp=active_jp,
        page_title=title.replace("RACAILLE | ", ""),
        last_updated_label=last_updated_label,
        date=date,
        content=content,
        link_terms=link_terms,
        link_privacy=link_privacy,
        link_refund=link_refund,
        designrush_text=designrush_text
    )

    with open(path, "w") as f:
        f.write(html)
    print(f"Created {path}")

# Create US files
create_file("US/privacy.html", privacy_content_us, "RACAILLE | Privacy Policy", "en", "US",
            ["Manifesto", "Services", "Portfolio", "Contact"],
            ["Terms", "Privacy Policy", "Refund Policy"],
            "Check out our listing on DesignRush")
create_file("US/refund.html", refund_content_us, "RACAILLE | Refund Policy", "en", "US",
            ["Manifesto", "Services", "Portfolio", "Contact"],
            ["Terms", "Privacy Policy", "Refund Policy"],
            "Check out our listing on DesignRush")

# Create ES files
create_file("ES/privacy.html", privacy_content_es, "RACAILLE | Política de Privacidad", "es", "ES",
            ["Manifiesto", "Servicios", "Portafolio", "Contacto"],
            ["Términos", "Política de Privacidad", "Política de Reembolso"],
            "Echa un vistazo a nuestro perfil en DesignRush")
create_file("ES/refund.html", refund_content_es, "RACAILLE | Política de Reembolso", "es", "ES",
            ["Manifiesto", "Servicios", "Portafolio", "Contacto"],
            ["Términos", "Política de Privacidad", "Política de Reembolso"],
            "Echa un vistazo a nuestro perfil en DesignRush")

# Create JP files
create_file("JP/privacy.html", privacy_content_jp, "RACAILLE | プライバシーポリシー", "ja", "JP",
            ["マニフェスト", "サービス", "ポートフォリオ", "お問い合わせ"],
            ["利用規約", "プライバシーポリシー", "返金ポリシー"],
            "DesignRushで私たちのプロフィールをご覧ください")
create_file("JP/refund.html", refund_content_jp, "RACAILLE | 返金ポリシー", "ja", "JP",
            ["マニフェスト", "サービス", "ポートフォリオ", "お問い合わせ"],
            ["利用規約", "プライバシーポリシー", "返金ポリシー"],
            "DesignRushで私たちのプロフィールをご覧ください")
