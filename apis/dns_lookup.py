import dns.resolver


def get_dns_records(domain: str) -> dict:

    results = {
        "A": [],
        "AAAA": [],
        "MX": [],
        "TXT": [],
        "NS": [],
        "errors": []
    }

    resolver = dns.resolver.Resolver(configure=False)

    resolver.nameservers = [
        "8.8.8.8",
        "1.1.1.1"
    ]

    record_types = [
        "A",
        "AAAA",
        "MX",
        "TXT",
        "NS"
    ]

    for record_type in record_types:

        try:

            answers = resolver.resolve(
                domain,
                record_type
            )

            for answer in answers:

                results[record_type].append(
                    str(answer)
                )

        except Exception as e:

            results["errors"].append(
                f"{record_type}: {str(e)}"
            )

    return results
