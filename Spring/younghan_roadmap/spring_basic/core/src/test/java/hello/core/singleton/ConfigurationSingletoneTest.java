package hello.core.singleton;

import hello.core.AppConfig;
import hello.core.AutoAppConfig;
import hello.core.member.repository.MemberRepository;
import hello.core.member.repository.MemoryMemberRepository;
import hello.core.member.service.MemberServiceImpl;
import hello.core.order.OrderServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class ConfigurationSingletoneTest {

    @Test
    @DisplayName("스프링 빈 싱글톤 테스트")
    void 테스트() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class);
        MemberServiceImpl memberService = ac.getBean( MemberServiceImpl.class);
        OrderServiceImpl orderService = ac.getBean( OrderServiceImpl.class);
        MemberRepository memberRepository = ac.getBean( MemoryMemberRepository.class);

        MemberRepository memberRepository1 = memberService.getMemberRepository();
        MemberRepository memberRepository2 = orderService.getMemberRepository();
        System.out.println("memberService -> memberRepository = " + memberRepository1);
        System.out.println("orderService -> memberRepository = " + memberRepository2);
        System.out.println("memberRepository = " + memberRepository);

        Assertions.assertThat(memberRepository1).isSameAs(memberRepository);
        Assertions.assertThat(memberRepository2).isSameAs(memberRepository);
    }

    @Test
    @DisplayName("Configure 테스트")
    void configurationDeep() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        AppConfig bean = ac.getBean("appConfig", AppConfig.class);

        System.out.println("AppConfig = " + bean.getClass());
    }
}
