package jpabook.jpashop.service;

import jpabook.jpashop.domain.item.Book;
import jpabook.jpashop.repository.ItemRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
@Transactional
class ItemServiceTest {

    @Autowired
    ItemService itemService;
    @Autowired
    ItemRepository itemRepository;

    @Test
    void 상품저장() {
        // given
        Book item = new Book();
        item.setName("JPA");
        item.setAuthor("김영한");

        // when
        itemService.saveItem(item);

        // then
        assertThat(itemRepository.findOne(item.getId())).isEqualTo(item);
    }

}