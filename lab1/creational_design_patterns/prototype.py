import copy

class Document:
    """
    Represents a document with a title, content, and related documents.
    """
    def __init__(self, title, content, related_documents=None):
        """
        Initializes a Document object.
        """
        self.title = title
        self.content = content
        self.related_documents = related_documents or []

    def add_related_document(self, document):
        """
        Adds a related document to the list.
        """
        self.related_documents.append(document)

    def __copy__(self):
        """
        Creates a shallow copy of the document.
        """
        new_document = Document(
            self.title,
            self.content,
            copy.copy(self.related_documents)  # Shallow copy of the list
        )
        return new_document

    def __deepcopy__(self, memo=None):
        """
        Creates a deep copy of the document.
        """
        if memo is None:
            memo = {}
        new_document = Document(
            self.title,
            copy.deepcopy(self.content, memo),
            copy.deepcopy(self.related_documents, memo)  # Deep copy of the list
        )
        return new_document

