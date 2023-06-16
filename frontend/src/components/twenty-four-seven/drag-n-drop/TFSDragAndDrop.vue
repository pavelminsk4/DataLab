<template>
  <div v-if="cardResults" class="drag-n-drop-wrapper">
    <div
      v-for="(itemStatus, index) in statuses"
      :key="'status' + index"
      :id="itemStatus.status"
      :class="[
        'drop-zone',
        isHighlighted(itemStatus.status) && 'highlighted',
        !itemStatus.isShow && 'hide-status',
        activeStatusCards.length === 1 && 'active-status',
      ]"
      @drop="onDrop($event, itemStatus.status)"
      @dragover="addBGToAvailColumn($event, itemStatus.status)"
      @mousedown="getCurrentColumnId(itemStatus.status)"
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

      <div :class="[activeStatusCards.length === 1 && 'drag-elements']">
        <TFSPostCard
          v-for="postInfo in getCardInformation(itemStatus.status)"
          :key="postInfo.id"
          :postDetails="postInfo.online_post"
          :is-back="postInfo.is_back"
          :card-status="postInfo.status"
          :item-id="postInfo.id"
          :is-work-button-show="true"
          draggable="true"
          class="drag-el"
          @change-status="changeStatus"
          @dragstart="startDrag($event, postInfo)"
          @open-modal="$emit('open-modal', postInfo)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TFSPostCard from '@/components/TFSPostCard'
import TFSColumnHeader from '@/components/twenty-four-seven/drag-n-drop/TFSColumnHeader'

const MIN_PAGES_NUMBER = 1

export default {
  name: 'TFSDragAndDrop',
  components: {TFSPostCard, TFSColumnHeader},
  props: {
    cardResults: {type: Object, reqared: true},
    currentStatuses: {type: Object, reqared: true},
  },
  data() {
    return {
      numberOfPage: 1,
      currentColumnName: null,
      newColumnName: null,
      highlightedColumns: [],
    }
  },
  computed: {
    statuses() {
      return this.currentStatuses
    },
    activeStatusCards() {
      return Object.values(this.statuses).filter((element) => element.isShow)
    },
  },
  methods: {
    getCardInformation(status) {
      return this.cardResults[status]?.results
    },

    startDrag($event, item) {
      $event.dataTransfer.dropEffect = 'move'
      $event.dataTransfer.effectAllowed = 'move'
      $event.dataTransfer.setData('itemId', item.id)

      this.highlightedColumns = this.statuses[item.status].allowedToDrag
    },

    onDrop($event, status) {
      this.highlightedColumns = []

      this.statuses[this.currentColumnName].allowedToDrag.filter(
        (allowedStatus) => {
          const postId = $event.dataTransfer.getData('itemId')
          if (allowedStatus === this.newColumnName) {
            this.$emit(
              'update-status',
              postId,
              this.statuses[status].status,
              this.statuses[this.currentColumnName].status,
              this.statuses[status].page,
              !this.isBack(this.statuses[status].status)
            )
          }
          return
        }
      )
    },

    isHighlighted(status) {
      return this.highlightedColumns.includes(status)
    },

    addBGToAvailColumn($event, index) {
      $event.preventDefault()
      this.newColumnName = this.statuses[index].status
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
      return this.findIndex(newStatus) >= this.findIndex(this.currentColumnName)
    },

    findIndex(statusName) {
      const statusesValue = Object.keys(this.statuses)
      return statusesValue.findIndex((el) => el.status === statusName)
    },

    getCurrentColumnId(statusName) {
      this.currentColumnName = statusName
    },
  },
}
</script>

<style lang="scss" scoped>
.drag-n-drop-wrapper {
  display: flex;
  justify-content: space-between;

  .drop-zone {
    display: flex;
    flex-direction: column;
    align-items: center;

    min-width: 320px;

    transition: all 0.3s;

    .drag-el {
      padding: 5px;
      margin-bottom: 10px;
      width: 290px;

      transition: all 0.3s;
    }
  }

  .hide-status {
    display: none;

    transition: all 0.3s;
  }

  .active-status {
    align-items: flex-start;

    margin: 0;
    min-width: 100%;

    transition: all 0.3s;

    .column-header {
      width: 100%;
    }
  }

  .drag-elements {
    display: flex;
    flex-wrap: wrap;

    gap: 12px;

    transition: all 0.3s;
  }

  .highlighted {
    background-color: #daf9ce;
  }
}

.drag-el:nth-last-of-type(1) {
  margin-bottom: 0;
}
</style>
