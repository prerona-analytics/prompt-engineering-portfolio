def generate_summary(metric, change, region):
    return f"{metric} changed by {change}% in {region}. Investigate causes."

print(generate_summary("Revenue", -12, "North"))
