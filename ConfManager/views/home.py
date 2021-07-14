def home(request):
    return HttpResponse("""
    <h1>Welcome to Lab Configuration Manager</h1>
    <p>Configurations</p>
    """)