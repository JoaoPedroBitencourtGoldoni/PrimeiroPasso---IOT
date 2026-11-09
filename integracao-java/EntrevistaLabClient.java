// Exemplo para adaptação no projeto Spring Boot (não é aplicação Java independente).
// Configure ENTREVISTALAB_URL e ENTREVISTALAB_INTERNAL_KEY via ambiente.
// Requer Spring Web; proteger endpoint Java com JWT e nunca enviar chave ao app Mobile.
package br.com.primeiropasso.integration;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;
import java.util.Map;
@Service
public class EntrevistaLabClient {
  private final RestClient client;
  public EntrevistaLabClient(@Value("${ENTREVISTALAB_URL:http://localhost:8000}") String url,
                            @Value("${ENTREVISTALAB_INTERNAL_KEY}") String key) {
    this.client = RestClient.builder().baseUrl(url)
      .defaultHeader("x-internal-api-key", key).build();
  }
  public Map gerarPergunta(Map<String,Object> payload) {
    return client.post().uri("/api/v1/entrevistas/pergunta").body(payload).retrieve().body(Map.class);
  }
  public Map gerarFeedback(Map<String,Object> payload) {
    return client.post().uri("/api/v1/entrevistas/feedback").body(payload).retrieve().body(Map.class);
  }
}
