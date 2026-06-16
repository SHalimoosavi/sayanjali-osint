def generate_ai_summary(report: dict) -> dict:

    risk_score = 50
    findings = []

    whois = report.get("whois", {})
    asn = report.get("asn_info", {})
    vt = report.get("virustotal", {})

    registrar = str(
        whois.get("registrar", "")
    ).lower()

    organization = str(
        asn.get("organization", "")
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

    for company in trusted_orgs:

        if company in organization:

            risk_score -= 20

            findings.append(
                f"Trusted organization detected: {organization}"
            )

            break

    for reg in trusted_registrars:

        if reg in registrar:

            risk_score -= 10

            findings.append(
                f"Trusted registrar detected: {registrar}"
            )

            break

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

    if vt:

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
                f"{malicious} malicious detections"
            )

        if suspicious > 0:

            risk_score += 20

            findings.append(
                f"{suspicious} suspicious detections"
            )

        if reputation > 100:

            risk_score -= 20

            findings.append(
                "High VirusTotal reputation"
            )

    risk_score = max(
        0,
        min(
            100,
            risk_score
        )
    )

    if risk_score <= 20:

        verdict = "Low Risk"

    elif risk_score <= 50:

        verdict = "Medium Risk"

    else:

        verdict = "High Risk"

    return {
        "risk_score": risk_score,
        "verdict": verdict,
        "findings": findings
    }
