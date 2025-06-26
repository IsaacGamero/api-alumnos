import boto3

def lambda_handler(event, context):
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
  
    response = table.delete_item(
      Key{
          'tenant_id': tenant_id,
          'alumno_id': alumno_id
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'message': f'Alumno {alumno_id} eliminado correctamente',
        'response': response
    }
