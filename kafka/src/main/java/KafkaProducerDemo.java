import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class KafkaProducerDemo {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "10.6.8.9:9001,10.6.8.9:9002,10.6.8.9:9003");
        props.put("acks", "all");
        props.put("retries", 0);
        props.put("batch.size", 16384);
        props.put("linger.ms", 1);
        props.put("buffer.memory", 33554432);
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<String, String>(props);
        for (int i = 0; i < 200; i++) {
//            ProducerRecord<String, String> record = new ProducerRecord<String, String>("mycp5-2", "hello"+ i);//topic，value
//            producer.send(record);
            producer.send(new ProducerRecord<String, String>("mycp5-2", Integer.toString(i), "hello"+Integer.toString(i))); //topic, key, value
        }

        producer.close();//不要忘记close
    }
}