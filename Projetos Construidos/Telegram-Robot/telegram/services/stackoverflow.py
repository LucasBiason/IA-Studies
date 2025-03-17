import requests, json, config

class StackOverFlowService():
    ''' Class of Service to connect 
    to StackOverflow and return the results obtained
    
    Params:
    - text: search text
    - type_text: type of interaction sending at chat
    
    Note:
    - put token string at config file
    '''

    def __init__(self, text, type_text=''):
        self.type_text = type_text
        self.params = self._prepare_params(text)
        self._make_request()
        
    def status_response(self):
        if self.response.status_code == 200:
            return True, ''
        elif self.type_text in ['document', 'sticker']:
            return False, 'Please insert only text'
        else:
            return False, 'No results found.'

    def json_response(self):
        return self.response.json().get('items')
    
    def _make_request(self):
        self.response = requests.get(
            config.URL,
            headers={
                'Authorization': config.TOKEN
            },
            params=self.params
        )
    
    def _prepare_params(self, text):
        return {
            'site': 'stackoverflow',
            'intitle': text,
            'order': 'desc',
            'sort': 'votes'
        }
    
    def get_messages_results(self):
        messages = []
        status, msg = self..status_response()
        
        if status:
            json_response = self.json_response()
            for question in json_response:
                texto = 'Title: {}\nVotes: {}\nLink: {}'.format(
                    question.get('title'),
                    question.get('score'),
                    question.get('link')
                )
                messages.append(texto)
        else:
            messages.append(msg)
        
        return messages
