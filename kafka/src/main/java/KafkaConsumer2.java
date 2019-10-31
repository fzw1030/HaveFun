import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;
import java.util.Arrays;
import java.util.Properties;

public class KafkaConsumer2 {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "10.6.8.9:9001,10.6.8.9:9002,10.6.8.9:9003");
        String group="y";
        props.put("group.id", group);//指定消费者属于哪个组
        props.put("enable.auto.commit", "false");
        props.put("auto.commit.interval.ms", "1000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        String topic="mycp5-2";
//        consumer.subscribe(Arrays.asList(topic));//指定消费的topic
       int avc = 1 ;
        while (avc == 1) {
            TopicPartition p = new TopicPartition(topic,4);
            consumer.assign(Arrays.asList(p));
            consumer.seek(p,466);
            //while (true) {
            ConsumerRecords<String, String> records = consumer.poll(100);

            for (ConsumerRecord<String, String> record : records) {
                Long a =record.offset();
                Long b =286L;

//                if ( a.equals(b)) {
                    System.out.printf("group = %s ,topic = %s, offset = %d, partition =%d , timestamp= %s, key = %s, value = %s%n",
                            group,topic,record.offset(), record.partition(),record.timestamp(),record.key(), record.value());
//                    avc = 0 ;
//                    break;
//                }

            }
      }
    }
}