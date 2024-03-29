package hello.core.member.service;

import hello.core.member.domain.Member;
import hello.core.member.repository.MemberRepository;
import hello.core.member.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MemberServiceImpl implements MemberService {

    // MemberServiceImpl이 MemoryMemberRepository와 의존관계로 DIP에 위배된다.
//    private final MemberRepository memberRepository = new MemoryMemberRepository();
    /**
     * MemberRepository 인터페이스에만 의존한다.
     */
    private final MemberRepository memberRepository;

    /**
     * MemberRepository 구현체를 외부에서 주입받는다. 구현체가 무엇일지는 외부에서 결정한다.
     */
    @Autowired
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }

    // 싱글톤 확인 테스트
    public MemberRepository getMemberRepository() {
        return memberRepository;
    }
}
