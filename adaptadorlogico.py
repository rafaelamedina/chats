#-*- coding: UTF-8 -*-
#ISSO ESTÁ EM TESTE AINDA!!

from chatterbot.logic import LogicAdapter
from chatterbot.adapters import Adapter
from chatterbot.storage import StorageAdapter
from chatterbot.search import IndexedTextSearch
from chatterbot.conversation import Statement
from chatterbot import filters

class LogicAdapter(Adapter):
    """
    Classe abstrata que representa o que os adaptadores lógicos farão.
    É importada diretamente na definição da instância do bot.

    :param search_algorithm_name: O nome dos algoritmo que faz a pesquisa do machine learning, 
    ou seja, faz a pesquisa no BD do bot para dar a resposta baseada em um nome. 
    Padrão: search_name

    :param maximum_similarity_threshold:
        O quanto o bot vai demorar para responder e, também, o quão eficiente a resposta vai ser.
        Quanto mais tempo demorar, menor a probabilidade da resposta vir errada. 
        Padrão: 0.95 segundos.

    :param response_selection_method:
          Método de seleção de resposta.
          Padrão: ``get_first_response``
    :type response_selection_method: collections.abc.Callable

    :param default_response:
          Uma resposta padrão para quando o bot
          não conseguir resposta. O padrão é justamente não ter uma respsota padrão.
    :type default_response: str ou list ou tuple
    """
    
#define a inicialização dos adaptadores
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        from chatterbot.response_selection import get_first_response

        self.search_algorithm_name = kwargs.get(
            'search_algorithm_name',
            IndexedTextSearch.name
        )

        self.search_algorithm = self.chatbot.search_algorithms[
            self.search_algorithm_name
        ]

        self.maximum_similarity_threshold = kwargs.get(
            'maximum_similarity_threshold', 0.95
        )

        # Seleciona a primeira resposta possível
        self.select_response = kwargs.get(
            'response_selection_method',
            get_first_response
        )

        default_responses = kwargs.get('default_response', [])

        # Converte uma string em uma lista.
        if isinstance(default_responses, str):
            default_responses = [
                default_responses
            ]

        self.default_responses = [
            Statement(text=default) for default in default_responses
        ]

	def can_process(self, statement):
        """
        Uma checagem para deterimnar se os adaptadores lógicos 
        podem processar os statment. Por padrão, sempre retorna verdadeiro, mas pode 
        ser modificado conforme necessidades.

        :tipo: bool
        """
        return True


	def get_default_response(self, input_statement):
        """
        Método usado quando o bot não tem capacidade de 
        escolher uma resposta maneira.
        """
        from random import choice

        if self.default_responses:
            response = choice(self.default_responses)
        else:
            try:
                response = self.chatbot.storage.get_random()
            except StorageAdapter.EmptyDatabaseException:
                response = input_statement

        self.chatbot.logger.info(
            'Selecionando resposta aleatória'
        )

        # tempo de resposta em 0 porque a resposta é aleatória, nesse caso. Sujeito a mudança.
        response.confidence = 0

        return response


    @property
    def class_name(self):
        """
        Retorna o nome da classe.
        Facilita nossa vida na hora de debugar e ver se tem algo de errado
        """
        return str(self.__class__.__name__)
