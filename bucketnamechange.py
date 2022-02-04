bucketname = input(" Enter the name of your bucket: ")
inputted_s3_uri = f"s3://{bucketname}"
replace_with_input_source = "s3://comprehend-semi-structured-documents-us-east-1-accountnumber/source-semi-structured-documents/"
input_source = f"{inputted_s3_uri}/source/"

replace_with_input_annotations = "s3://comprehend-semi-structured-documents-us-east-1-accountnumber/output/legal-entity-label-job-labeling-job-20220104T172242/annotations/consolidated-annotation/consolidation-response/iteration-1/"
input_annotations =  f"{inputted_s3_uri}/"

with open("output.manifest") as output_file:
    data = output_file.read()
    data = data.replace(replace_with_input_source, input_source)
    data = data.replace(replace_with_input_annotations, input_annotations)
    with open("output.manifest", "w") as parsed_output_file:
        parsed_output_file.write(data)

print("The manifest file is updated with the correct bucket")