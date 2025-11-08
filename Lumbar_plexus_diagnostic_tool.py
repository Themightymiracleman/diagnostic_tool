# Lumbar Plexus Diagnostic Tool
# Author: Brenden Nichols
# Description: Asks about lumbar plexus-related symptoms and suggests possible diagnoses.

def lumbar_diagnostic():
    print("=== Lumbar Plexus Diagnostic Tool ===\n")
    print("Please answer 'yes' or 'no' to the following symptoms.\n")

    symptoms = {}

    symptoms["anterior_thigh_pain"] = input("Pain or numbness in the anterior thigh? ").strip().lower() == "yes"
    symptoms["medial_thigh_pain"] = input("Pain or numbness in the medial thigh? ").strip().lower() == "yes"
    symptoms["lateral_thigh_pain"] = input("Burning or tingling on the lateral thigh (outer thigh)? ").strip().lower() == "yes"
    symptoms["knee_extension_weakness"] = input("Weakness when extending the knee? ").strip().lower() == "yes"
    symptoms["hip_adduction_weakness"] = input("Weakness bringing the legs together (adduction)? ").strip().lower() == "yes"
    symptoms["groin_pain"] = input("Pain or numbness in the groin or inner thigh? ").strip().lower() == "yes"
    symptoms["abdominal_wall_weakness"] = input("Weakness in the lower abdominal wall? ").strip().lower() == "yes"

    print("\nAnalyzing responses...\n")

    possible_diagnoses = []

    # Femoral nerve involvement
    if symptoms["anterior_thigh_pain"] or symptoms["knee_extension_weakness"]:
        possible_diagnoses.append("Femoral nerve neuropathy or L2–L4 radiculopathy")

    # Obturator nerve
    if symptoms["medial_thigh_pain"] or symptoms["hip_adduction_weakness"]:
        possible_diagnoses.append("Obturator nerve entrapment or L3–L4 root irritation")

    # Lateral femoral cutaneous nerve
    if symptoms["lateral_thigh_pain"]:
        possible_diagnoses.append("Meralgia paresthetica (lateral femoral cutaneous nerve entrapment)")

    # Ilioinguinal or genitofemoral
    if symptoms["groin_pain"]:
        possible_diagnoses.append("Ilioinguinal or genitofemoral neuralgia (L1–L2)")

    # Iliohypogastric
    if symptoms["abdominal_wall_weakness"]:
        possible_diagnoses.append("Iliohypogastric nerve injury (L1)")

    if not possible_diagnoses:
        print("No clear pattern detected. Consider non-lumbar causes or refer for imaging/EMG studies.")
    else:
        print("Possible diagnoses based on your responses:")
        for d in possible_diagnoses:
            print(f" - {d}")

    print("\nThis tool is for educational purposes only and does not replace professional medical evaluation.")

if __name__ == "__main__":
    lumbar_diagnostic()
