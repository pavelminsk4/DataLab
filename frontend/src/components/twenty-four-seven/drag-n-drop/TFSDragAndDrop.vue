<template>
  <div v-if="cardResults" class="drag-n-drop-wrapper">
    <div
      v-for="(itemStatus, index) in statuses"
      :key="'status' + index"
      :id="itemStatus.status"
      class="drop-zone"
      @drop="onDrop($event, index)"
      @dragover="addBGToAvailColumn($event, index)"
      @mousedown="getCurrentColumnId(index)"
      @dragenter.prevent
    >
      <TFSColumnHeader
        v-model="itemStatus.page"
        :value="itemStatus.page"
        :status="itemStatus.status"
        :status-color="itemStatus.color"
        :number-of-pages="numberOfPages(itemStatus.status)"
        :number-of-results="this.cardResults[itemStatus.status]?.count"
        @update-page="updatePage"
        @decrease-arrow="decrease(index, itemStatus.status)"
        @increase-arrow="increase(index, itemStatus.status)"
      />

      <div
        v-for="postInfo in getCardInformation(itemStatus.status)"
        :key="postInfo.id"
        class="drag-el"
        draggable="true"
        @dragstart="startDrag($event, postInfo)"
      >
        <TFSPostCard
          :postDetails="postInfo.online_post"
          :is-back="postInfo.is_back"
          :card-status="postInfo.status"
          :item-id="postInfo.id"
          :is-work-button-show="true"
          class="post-card"
          @change-status="changeStatus"
          @open-modal="$emit('open-modal', postInfo)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {dragAndDropStatuses} from '@/lib/configs/tfsStatusesConfig'

import TFSPostCard from '@/components/TFSPostCard'
import TFSColumnHeader from '@/components/twenty-four-seven/drag-n-drop/TFSColumnHeader'

const MIN_PAGES_NUMBER = 1

export default {
  name: 'TFSDragAndDrop',
  components: {TFSPostCard, TFSColumnHeader},
  props: {
    cardResults: {type: Object, reqared: true},
  },
  data() {
    return {
      numberOfPage: 1,
      currentColumnId: null,
      newAreaId: null,
    }
  },
  created() {
    this.statuses = dragAndDropStatuses
  },
  methods: {
    getCardInformation(status) {
      return this.cardResults[status]?.results
    },

    startDrag($event, item) {
      $event.dataTransfer.dropEffect = 'move'
      $event.dataTransfer.effectAllowed = 'move'
      $event.dataTransfer.setData('itemId', item.id)
    },

    onDrop($event, index) {
      this.statuses[this.currentColumnId].allowedToDrag.filter(
        (allowedStatus) => {
          const postId = $event.dataTransfer.getData('itemId')

          let allowedElement = document.getElementById(allowedStatus)
          allowedElement.style.background = ''
          if (allowedStatus === this.newAreaId) {
            this.$emit(
              'update-status',
              postId,
              this.statuses[index].status,
              this.statuses[this.currentColumnId].status,
              this.statuses[index].page,
              !this.isBack(this.statuses[index].status)
            )
          }
          return
        }
      )
    },

    addBGToAvailColumn($event, index) {
      $event.preventDefault()

      this.newAreaId = this.statuses[index].status
      this.statuses[this.currentColumnId].allowedToDrag.filter((el) => {
        if (el === $event.target.id) {
          $event.target.style.background = '#DAF9CE'
        }
        return
      })
    },

    changeStatus(itemId, newStatus, oldStatus) {
      this.$emit(
        'change-status-via-dropdown',
        itemId,
        newStatus,
        oldStatus,
        this.numberOfPage,
        !this.isBack(newStatus)
      )
    },

    increase(index, status) {
      if (this.statuses[index].page >= this.countOfPages(status)) return

      this.statuses[index].page = +this.statuses[index].page + 1
      let newPageValue = this.statuses[index].page

      this.updatePage(newPageValue, status)
    },

    decrease(index, status) {
      if (this.statuses[index].page <= MIN_PAGES_NUMBER) return

      this.statuses[index].page -= 1
      let newPageValue = this.statuses[index].page

      this.updatePage(newPageValue, status)
    },

    updatePage(page, status) {
      this.$emit('update-page', page, status)
    },

    countOfPages(status) {
      return Math.ceil(this.cardResults[status]?.count / 20)
    },

    numberOfPages(status) {
      return Array.from({length: this.countOfPages(status)}, (_, i) => +i + 1)
    },

    isBack(newStatus) {
      let newStatusIndex = this.statuses.findIndex(
        (el) => el.status === newStatus
      )

      return newStatusIndex >= this.currentColumnId
    },

    getCurrentColumnId(id) {
      this.currentColumnId = id
    },
  },
}
</script>

<style lang="scss" scoped>
.drag-n-drop-wrapper {
  display: flex;

  .drop-zone {
    min-width: 320px;
    margin: 50px auto;
    padding: 10px;

    .drag-el {
      padding: 5px;
      margin-bottom: 10px;

      .post-card {
        width: 290px;
      }
    }
  }
}

.drag-el:nth-last-of-type(1) {
  margin-bottom: 0;
}
</style>
