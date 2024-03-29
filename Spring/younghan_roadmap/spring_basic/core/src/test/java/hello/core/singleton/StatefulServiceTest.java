package hello.core.singleton;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import static org.assertj.core.api.Assertions.assertThat;

public class StatefulServiceTest {
    @Test
    @DisplayName("싱글톤에서 공유필드 썼을 때 문제 예시")
    void statefulField() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(StatefulServiceConfig.class);
        StatefulService threadA = ac.getBean("statefulService", StatefulService.class);
        StatefulService threadB = ac.getBean("statefulService", StatefulService.class);

        // 공유 필드로 인해 threadA의 price가 20000으로 바뀜
//        threadA.order("threadA", 10000);
//        threadB.order("threadB", 20000);
//        int price = threadA.getPrice();
//        System.out.println("price = "+price);
//        assertThat(price).isEqualTo(20000);
    }

    @Test
    @DisplayName("지역변수를 이용하며 공유필드 제거")
    void statelessField() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(StatefulServiceConfig.class);
        StatefulService threadA = ac.getBean("statefulService", StatefulService.class);
        StatefulService threadB = ac.getBean("statefulService", StatefulService.class);

        int threadAPrice = threadA.order("threadA", 10000);
        int threadBPrice = threadB.order("threadB", 20000);
        System.out.println("price = "+threadAPrice);
        assertThat(threadAPrice).isEqualTo(10000);
    }

    static class StatefulServiceConfig {
        @Bean
        public StatefulService statefulService() {
            return new StatefulService();
        }
    }
}
