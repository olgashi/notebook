import datetime

last_id = 0

class Note:
	'''Note in a notebook, performs string searches, stores note tags.'''

	def __init__(self, memo, tags=''):
		'''initialize note with memo and optional tags, set the date of 
		when the note was created, set unique id'''
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		'''Return true if the note matches filter text, false otherwise.'''

		return filter in self.memo or filter in self.tags

class Notebook:
    '''Collection of notes. Notes can be modified, searched and tagged'''
    
    def __init__(self):
        '''Initialize notebook with an empty list'''
        self.notes = []
    
    def new_note(self, memo, tags=''):
        '''Create a new note, add to the list'''
        self.notes.append(Note(memo, tags))
    
    def _find_note(self, note_id):
        '''Locate note with a given id'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
    def modify_memo(self, note_id, memo):
        '''Find note with a given id, change memo to a given value'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
        
    def modify_tags(self, note_id, tags):
        '''Find note with given id and change its tags to a given value'''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
    
    def search(self, filter):
        '''Find all notes matching given filter string.'''
        return [note for note in self.notes if note.match(filter)]