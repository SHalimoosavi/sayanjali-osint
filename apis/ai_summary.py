def generate_ai_summary(report: dict) -> dict:

    findings = []

    query_type = report.get(
        "query_type",
        ""
    )

    # =====================================
    # GEOLOCATION / ADDRESS INVESTIGATIONS
    # =====================================

    if query_type in [
        "coordinates",
        "address"
    ]:

        nearby = report.get(
            "nearby_places",
            {}
        )

        total_places = nearby.get(
            "total_results",
            len(
                nearby.get(
                    "results",
                    []
                )
            )
        )

        if total_places > 0:

            findings.append(
                f"{total_places} nearby locations discovered"
            )

        else:

            findings.append(
                "No nearby locations discovered"
            )

        return {
            "risk_score": 0,
            "verdict": "Informational",
            "confidence": 90,
            "findings": findings
        }

    # =====================================
    # THREAT INVESTIGATION
    # =====================================

    risk_score = 50

    whois = report.get("whois", {})
    asn = report.get("asn_info", {})
    vt = report.get("virustotal", {})
    abuse = report.get("abuseipdb", {})
    otx = report.get("otx", {})
    shodan = report.get("shodan", {})
    threat_feed = report.get("threat_feed", {})

    registrar = str(
        whois.get(
            "registrar",
            ""
        )
    ).lower()

    organization = str(
        asn.get(
            "organization",
            ""
        )
    ).lower()

    trusted_orgs = [
        "google",
        "microsoft",
        "amazon",
        "cloudflare",
        "meta",
        "github",
        "apple"
    ]

    trusted_registrars = [
        "markmonitor",
        "godaddy",
        "hostinger",
        "namecheap",
        "cloudflare"
    ]

    # =====================================
    # TRUSTED ORGANIZATION
    # =====================================

    for company in trusted_orgs:

        if company in organization:

            risk_score -= 20

            findings.append(
                f"Trusted organization detected: {organization}"
            )

            break

    # =====================================
    # TRUSTED REGISTRAR
    # =====================================

    for reg in trusted_registrars:

        if reg in registrar:

            risk_score -= 10

            findings.append(
                f"Trusted registrar detected: {registrar}"
            )

            break

    # =====================================
    # DNS ANALYSIS
    # =====================================

    dns_records = report.get(
        "dns_records",
        {}
    )

    if dns_records.get("MX"):

        risk_score -= 5

        findings.append(
            "Email infrastructure detected"
        )

    if dns_records.get("NS"):

        risk_score -= 5

        findings.append(
            "Name servers configured"
        )

    # =====================================
    # VIRUSTOTAL
    # =====================================

    if vt and not vt.get("error"):

        malicious = vt.get(
            "malicious",
            0
        )

        suspicious = vt.get(
            "suspicious",
            0
        )

        reputation = vt.get(
            "reputation",
            0
        )

        if malicious > 0:

            risk_score += 40

            findings.append(
                f"{malicious} VirusTotal malicious detections"
            )

        if suspicious > 0:

            risk_score += 20

            findings.append(
                f"{suspicious} VirusTotal suspicious detections"
            )

        if reputation > 100:

            risk_score -= 20

            findings.append(
                "High VirusTotal reputation"
            )

    # =====================================
    # ABUSEIPDB
    # =====================================

    if abuse and not abuse.get("error"):

        abuse_score = abuse.get(
            "abuse_score",
            0
        )

        reports = abuse.get(
            "total_reports",
            0
        )

        if abuse_score >= 75:

            risk_score += 40

            findings.append(
                f"AbuseIPDB high confidence abuse ({abuse_score})"
            )

        elif abuse_score >= 25:

            risk_score += 20

            findings.append(
                f"AbuseIPDB moderate abuse score ({abuse_score})"
            )

        elif abuse_score == 0:

            risk_score -= 10

            findings.append(
                "No AbuseIPDB abuse confidence"
            )

        if reports > 100:

            findings.append(
                f"{reports} AbuseIPDB reports"
            )

    # =====================================
    # OTX
    # =====================================

    if otx and not otx.get("error"):

        pulse_count = otx.get(
            "pulse_count",
            0
        )

        if pulse_count > 0:

            risk_score += min(
                pulse_count,
                20
            )

            findings.append(
                f"Referenced in {pulse_count} OTX pulses"
            )

    # =====================================
    # SHODAN
    # =====================================

    if shodan and not shodan.get("error"):

        ports = shodan.get(
            "ports",
            []
        )

        port_count = len(
            ports
        )

        if port_count > 20:

            risk_score += 20

            findings.append(
                f"Large attack surface ({port_count} ports)"
            )

        elif port_count > 5:

            risk_score += 10

            findings.append(
                f"Multiple exposed services ({port_count} ports)"
            )

    # =====================================
    # THREAT FEED CORRELATION
    # =====================================

    threat_score = threat_feed.get(
        "threat_score",
        0
    )

    if threat_score > 0:

        risk_score += min(
            threat_score,
            40
        )

        findings.append(
            f"Threat feed score {threat_score}"
        )

    if threat_feed.get("malicious_ips"):

        findings.append(
            "Known malicious IP detected"
        )

    if threat_feed.get("malicious_domains"):

        findings.append(
            "Known malicious domain detected"
        )

    if threat_feed.get("malicious_emails"):

        findings.append(
            "Known malicious email detected"
        )

    if threat_feed.get("malicious_urls"):

        findings.append(
            "Known malicious URL detected"
        )

    # =====================================
    # NORMALIZE
    # =====================================

    risk_score = max(
        0,
        min(
            100,
            risk_score
        )
    )

    # =====================================
    # VERDICT
    # =====================================

    if risk_score <= 20:

        verdict = "Low Risk"

    elif risk_score <= 50:

        verdict = "Medium Risk"

    elif risk_score <= 75:

        verdict = "High Risk"

    else:

        verdict = "Critical Risk"

    confidence = round(
        min(
            100,
            50 + len(findings) * 5
        ),
        0
    )

    return {
        "risk_score": risk_score,
        "verdict": verdict,
        "confidence": confidence,
        "findings": findings
    }
