import phonenumbers
from phonenumbers import geocoder, carrier, timezone, NumberParseException, PhoneNumberType

def analyze_phone_number(number):
    try:
        # Telefon numarasını ayrıştır
        parsed_number = phonenumbers.parse(number)

        # Ülke bilgisini al
        country = geocoder.description_for_number(parsed_number, "en")

        # Taşıyıcı (operatör) bilgisini al
        phone_carrier = carrier.name_for_number(parsed_number, "en")

        # Telefon numarasının zaman dilimini al
        phone_timezones = timezone.time_zones_for_number(parsed_number)

        # Telefon numarasının formatını kontrol et
        valid_number = phonenumbers.is_valid_number(parsed_number)

        # Telefon numarasının aktif olup olmadığını kontrol et
        possible_number = phonenumbers.is_possible_number(parsed_number)

        # Uluslararası formatı al
        international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        # Ulusal formatı al
        national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

        # Telefon numarası türünü belirle
        number_type = phonenumbers.number_type(parsed_number)

        return {
            "country": country,
            "carrier": phone_carrier,
            "timezones": phone_timezones,
            "is_valid": valid_number,
            "is_possible": possible_number,
            "international_format": international_format,
            "national_format": national_format,
            "number_type": number_type
        }
    except NumberParseException:
        return "Geçersiz numara formatı."

# Örnek bir telefon numarası ile fonksiyonu test et
test_number = "+901111111111"  # Örnek bir Türkiye numarası
analyze_result = analyze_phone_number(test_number)
print(analyze_result)
