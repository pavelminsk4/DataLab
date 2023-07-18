<template>
  <BaseModal
    title="Add link to report"
    modal-frame-style="max-width:90vw;"
    class="working-modal"
  >
    <div v-if="publishingPosts?.length" class="cards">
      <TFSPostCard
        v-for="postInfo in publishingPosts"
        :key="postInfo.id"
        :postDetails="postInfo.online_post"
        :is-back="postInfo.is_back"
        :card-status="postInfo.status"
        :item-id="postInfo.id"
        :is-checkbox-show="true"
        :is-show-statuses-dropdown="false"
        :selected-post="addedPost(postInfo)"
        @add-related-content="addLinkedContent"
      />
    </div>

    <div v-else>There are no posts with the publishing status! &#128531;</div>

    <PaginationControlPanel
      v-if="numberOfPages"
      v-model="currentPage"
      :pages="numberOfPages"
      :is-show-count-posts="false"
      @update-page="updatePage"
    />
  </BaseModal>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import TFSPostCard from '@/components/TFSPostCard'
import PaginationControlPanel from '@/components/PaginationControlPanel'

const {mapState, mapActions} = createNamespacedHelpers('twentyFourSeven')

const PUBLISHING = 'Publishing'

export default {
  name: 'TFSLibkedPostsModal',
  components: {BaseModal, TFSPostCard, PaginationControlPanel},
  props: {
    selectedLinkedPost: {type: Object, required: true},
  },
  data() {
    return {
      currentPage: 1,
    }
  },
  computed: {
    ...mapState(['items']),
    publishingPosts() {
      let posts = this.items[PUBLISHING]?.results

      return posts?.sort((firstEl, secondEl) => firstEl.id - secondEl.id)
    },
    numberOfPages() {
      const publishingPostsCount = this.items[PUBLISHING]?.count
      return publishingPostsCount ? Math.ceil(publishingPostsCount / 20) : 1
    },
  },
  methods: {
    ...mapActions([action.UPDATE_TFS_ITEM_DATA]),
    addedPost(post) {
      return post.linked_items.some(
        (linkedPost) => linkedPost.id === this.selectedLinkedPost.id
      )
    },
    updatePage(page) {
      this.$emit('update-page', page, PUBLISHING)
    },
    addLinkedContent(isChecked, postId) {
      const currentCheckedPost = this.publishingPosts.find(
        (post) => post.id === postId
      )
      const linkedItemsIds = currentCheckedPost?.linked_items.map(
        (item) => item.id
      )

      if (isChecked) {
        linkedItemsIds.push(this.selectedLinkedPost.id)
      } else {
        linkedItemsIds?.filter((el) => el !== this.selectedLinkedPost.id)
      }

      this.updateLinkedPosts(linkedItemsIds, postId)
    },

    async updateLinkedPosts(linkedItemsIds, postId) {
      try {
        await this[action.UPDATE_TFS_ITEM_DATA]({
          projectId: this.selectedLinkedPost.project,
          postId: postId,
          value: {
            status: PUBLISHING,
            linked_items: linkedItemsIds,
          },
          page: 1,
        })
      } catch (e) {
        console.error(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;

  margin-bottom: 24px;
}
</style>
