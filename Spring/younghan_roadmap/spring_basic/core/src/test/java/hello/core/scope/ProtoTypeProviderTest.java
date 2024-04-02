package hello.core.scope;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import jakarta.inject.Provider;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Scope;

import static org.assertj.core.api.Assertions.assertThat;

public class ProtoTypeProviderTest {

    @Test
    void providerTest() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(ClientBean.class, ProtoTypeBean.class);
        ClientBean clientBean1 = ac.getBean(ClientBean.class);
        int count1 = clientBean1.logic();
        assertThat(count1).isEqualTo(1);

        ClientBean clientBean2 = ac.getBean(ClientBean.class);
        int count2 = clientBean2.logic();
        assertThat(count2).isEqualTo(1);
    }

    @Scope("singleton")
    static class ClientBean {
        // 스프링 컨테이너 주입 방식, 스프링에 의존
//        private final ApplicationContext ac;
//        @Autowired
//        public ClientBean(ApplicationContext ac) {
//            this.ac = ac;
//        }
        // ObjectProvider 방식, 스프링에 의존
//        private final ObjectProvider<ProtoTypeBean> protoTypeBeanProvider;
//        @Autowired
//        ClientBean(ObjectProvider<ProtoTypeBean> protoTypeBeanProvider) {
//            this.protoTypeBeanProvider = protoTypeBeanProvider;
//        }
        // JSR-330 Provider 방식, 자바 표준
        private final Provider<ProtoTypeBean> protoTypeBeanProvider;

        @Autowired
        ClientBean(Provider<ProtoTypeBean> protoTypeBeanProvider) {
            this.protoTypeBeanProvider = protoTypeBeanProvider;
        }


        public int logic() {
//            ProtoTypeBean protoTypeBean = ac.getBean(ProtoTypeBean.class);
//            ProtoTypeBean protoTypeBean = protoTypeBeanProvider.getObject();
            ProtoTypeBean protoTypeBean = protoTypeBeanProvider.get();
            protoTypeBean.addCount();
            return protoTypeBean.getCount();
        }
    }

    @Scope("prototype")
    static class ProtoTypeBean {
        private int count = 0;

        public void addCount() {
            count++;
        }

        public int getCount() {
            return count;
        }

        @PostConstruct
        public void init() {
            System.out.println("ProtoTypeBean.init " + this);
        }

        @PreDestroy
        public void destroy() {
            System.out.println("ProtoTypeBean.destroy");
        }
    }
}
