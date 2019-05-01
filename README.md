# aria-document-generator

## Brief Description

ARIA is a full-stack web application meant to help server the Northern Nevada Music Teachers Association (NNMTA). The document engine is a component of this full-stack application that is meant to handle document generation requests by administrators for musical events.

## Authors
1. Anthony Bennett
2. Kevin Carlos
3. Nikkolas Irwin

## Link to ARIA (main application)
[ARIA](https://github.com/invainn/ARIA)

## Immediate Goals
- [x] Setup repository
- [ ] Create the template for at least one document used by NNMTA
- [ ] Hook the document generator to the main web application using Flask
- [ ] Show a proof of concept to stakeholders

## Future Work
- [ ] Add all remaining documents to document generator
- [ ] Evaluate future needs of NNMTA for new document(s)

# To Run
```
$env:FLASK_APP = "main"
flask run --port=4321
```

## Dependencies
### Package  Version
------------ -------
* Click        7.0
* Flask        1.0.2
* itsdangerous 1.1.0
* Jinja2       2.10.1
* lxml         4.3.3
* MarkupSafe   1.1.1
* pip          19.0.3
* python-docx  0.8.10
* setuptools   40.8.0
* Werkzeug     0.15.2
