import re


def lambda_handler(event, context):
    ''' Main function for AWS lambda. Requires output in JSON '''
    logline = event['LogName']

    error_type_1 = "status=bounced"
    error_type_2 = "status=deferred"

    if re.search(error_type_1, logline):
        print(('Looking for "%s" in "%s" ->' % (error_type_1, logline)))
        error_analysis = ("There is a bounced email - possible causes are"
                          " non-existent user or domain.")
    elif re.search(error_type_2, logline):
        print(('Looking for "%s" in "%s" ->' % (error_type_2, logline)))
        error_analysis = ("There is a deferred email - possible causes include"
                          " server not reacheable, or the server is actively"
                          " blocking our connections.")
    else:
        error_analysis = "There is No PostFix Errors in the Given Input"

    return {
        "Result": error_analysis,
    }
