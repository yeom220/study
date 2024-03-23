package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {

    /**
     * 직접 생성하는 경우 인스턴스가 달라져 테스트가 예상과 다르게 나올 수 있다. 여기서는 store 가 static 변수여서
     * 같은 데이터에 접근하여 테스트는 통과된다. 하지만 아래의 방식은 좋지 않다. DI를 활용하는게 여러모로 이점이 많다.
     */
//    MemberService memberService = new MemberService();
//    MemoryMemberRepository memberRepository = new MemoryMemberRepository();

    MemoryMemberRepository memberRepository;
    // DI
    MemberService memberService;

    /**
     * @BeforeEach : 각 테스트 실행 전에 호출된다. 테스트가 서로 영향이 없도록 항상 새로운 객체를 생성하고,
     * 의존관계도 새로 맺어준다.
     */
    @BeforeEach
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);   // DI
    }


    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }

    /**
     * 테스트케이스의 경우 실제 서비스에 사용되지 않기에 가독성 좋게 한글로 작성하기도 한다.
     */
    @Test
    void 회원가입() {
        // given
        Member member = new Member();
        member.setName("spring");

        // when
        Long id = memberService.join(member);

        // then
        Member findMember = memberService.findOne(id).get();
//        assertThat(findMember).isEqualTo(member);
        assertEquals(member.getName(), findMember.getName());
    }

    @Test
    void 중복_회원_예외() {
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        memberService.join(member1);

        // then
        IllegalStateException e = assertThrows(IllegalStateException.class,
                () -> memberService.join(member2)); // 예외가 발생해야 한다.

        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다."); // 예외 메시지 비교
    }
}