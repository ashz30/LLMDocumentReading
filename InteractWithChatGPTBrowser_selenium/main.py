import StructuredDocumentRead
import UnstructuredDocumentRead

unStructuredDocumentsFolderpath = "C:/GIT/LLMDocumentReading/Sample Contracts"
queryList = "which entity or product is the license for? , Does the contract cover retail sale?  "
UnstructuredDocumentRead.readDocuments(unStructuredDocumentsFolderpath, queryList)

structuredDocumentsFolderpath = "C:/GIT/LLMDocumentReading/sample invoices"
StructuredDocumentRead.readDocuments(structuredDocumentsFolderpath)